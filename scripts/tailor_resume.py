#!/usr/bin/env python3
"""Tailor Tyler's resume to a job description using Claude.

Drop a job description into job-descriptions/ and run this script. For each
job description it writes a tailored resume to tailored-resumes/ and reports
any requirement the knowledge base cannot support with real evidence.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Literal

import anthropic
from pydantic import BaseModel, Field

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "backend"))

from app.context import fetch_resume_text  # noqa: E402

JD_DIR = REPO_ROOT / "job-descriptions"
OUT_DIR = REPO_ROOT / "tailored-resumes"
KNOWLEDGE_BASE = REPO_ROOT / "knowledge_base.md"
TFVARS = REPO_ROOT / "infrastructure" / "terraform" / "terraform.tfvars"

MODEL = "claude-sonnet-5"
JD_SUFFIXES = {".md", ".txt"}
JD_IGNORED = {"readme.md"}


class KnowledgeGap(BaseModel):
    requirement: str = Field(
        description="The skill, tool, or experience this job asks for that the knowledge base has no real evidence of."
    )
    severity: Literal["blocking", "important", "nice-to-have"] = Field(
        description="How central this requirement is to the role."
    )
    question: str = Field(
        description="A specific question to ask Tyler whose answer would fill this gap. Ask for concrete detail: what he built, the scale, the outcome. Never a yes/no question."
    )


class TailoredResume(BaseModel):
    role_title: str = Field(
        description="The job title this resume is tailored for.")
    company: str = Field(
        description="The hiring company, or 'Unknown' if the description does not name one.")
    match_strength: Literal["Strong", "Good", "Partial", "Weak"]
    match_reasoning: str = Field(
        description="Two or three sentences of honest reasoning about the fit, gaps included.")
    tailored_resume: str = Field(
        description="The complete tailored resume as Markdown, ready to read on its own. Every claim must trace to the knowledge base or existing resume."
    )
    tailoring_notes: list[str] = Field(
        description="What was emphasized, reordered, or cut for this role, and why. One line each."
    )
    knowledge_gaps: list[KnowledgeGap] = Field(
        description="Requirements the knowledge base cannot back up. Empty if the knowledge base covers the role well."
    )


SYSTEM_PROMPT = """\
You are a resume editor working for Tyler Du, a software engineer. You tailor his \
resume to a specific job description.

Your sources of truth are below. They are the ONLY place facts may come from.

== Current Resume ==
{resume_text}

== Professional Knowledge Base ==
{knowledge_base}

Rules:

1. Never invent. Every bullet, metric, date, technology, and claim in the tailored \
resume must trace back to something in the sources above. If the job description asks \
for something Tyler has not done, you do not write it into the resume. You record it as \
a knowledge gap instead.

2. Tailor by selection and emphasis, not fabrication. The knowledge base holds far more \
detail than fits on one page. Your job is to choose the experiences that matter for THIS \
role, lead with them, and phrase them in the vocabulary the job description uses, as long \
as the rephrasing stays true to what actually happened.

3. Prefer specifics. A bullet with a number, a scale, or a named technology beats a vague \
one. The knowledge base has metrics; use them.

4. Keep it to roughly one page of Markdown: a short summary line, then Experience, \
Projects, Skills, and Education. Order sections so the most relevant material for this \
role comes first. Drop material that does not serve this application.

5. Placeholders marked [TODO: ...] in the knowledge base are unanswered questions, not \
facts. Never treat their content as real experience. If a TODO sits on something this \
role needs, that is a knowledge gap.

6. Be honest in match_strength and match_reasoning. A recruiter reading an inflated \
assessment is worse off than one reading an accurate one.

7. Knowledge gaps are the most valuable thing you produce. When the role needs something \
the sources do not cover, write a question specific enough that Tyler's answer could be \
pasted straight into the knowledge base. "Have you used Kubernetes?" is a bad question. \
"Have you deployed or operated anything on Kubernetes, and if so, what was running on it \
and roughly what scale?" is a good one. If Tyler genuinely has relevant experience for \
every requirement, return an empty list rather than manufacturing concerns.

8. Never use em dashes (the character) anywhere in your output. Use commas, periods, \
colons, or parentheses instead. This applies to the resume and to every other field.\
"""


def load_api_key() -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    if TFVARS.exists():
        match = re.search(
            r'^\s*anthropic_api_key\s*=\s*"([^"]+)"', TFVARS.read_text(
                encoding="utf-8"), re.MULTILINE
        )
        if match:
            return match.group(1)
    return None


def tailor(client: anthropic.Anthropic, jd_text: str, resume_text: str, knowledge_base: str) -> TailoredResume:
    system = SYSTEM_PROMPT.format(
        resume_text=resume_text, knowledge_base=knowledge_base)
    with client.messages.stream(
        model=MODEL,
        max_tokens=32000,
        system=system,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        output_format=TailoredResume,
        messages=[{"role": "user", "content": f"Job Description:\n\n{jd_text}"}],
    ) as stream:
        return stream.get_final_message().parsed_output


def strip_em_dashes(text: str) -> str:
    """Em dashes are banned in this project's text. Pipes suit list-style lines, commas suit prose."""
    return "\n".join(
        line.replace(" — ", " | " if " | " in line else ", ").replace("—", ",")
        for line in text.splitlines()
    )


def render(result: TailoredResume, jd_path: Path) -> str:
    title = result.role_title
    if result.company.lower() not in title.lower():
        title = f"{title} at {result.company}"

    lines = [
        f"# {title}",
        "",
        f"*Tailored from `{jd_path.name}` | Match: **{result.match_strength}***",
        "",
        result.match_reasoning,
        "",
        "---",
        "",
        result.tailored_resume,
        "",
        "---",
        "",
        "## Tailoring Notes",
        "",
    ]
    lines += [f"- {note}" for note in result.tailoring_notes]

    if result.knowledge_gaps:
        lines += ["", "## Knowledge Base Gaps", ""]
        lines.append(
            "The knowledge base has no evidence for the following. Answer these and add "
            "them to `knowledge_base.md` so future tailoring can draw on them."
        )
        lines.append("")
        for gap in result.knowledge_gaps:
            lines += [f"### {gap.requirement}  `{gap.severity}`",
                      "", gap.question, ""]
    else:
        lines += ["", "## Knowledge Base Gaps", "",
                  "None. The knowledge base covers this role."]

    return strip_em_dashes("\n".join(lines) + "\n")


def report_gaps(result: TailoredResume) -> None:
    if not result.knowledge_gaps:
        print("  No knowledge base gaps for this role.")
        return

    print(f"  {len(result.knowledge_gaps)} knowledge base gap(s). Answer these to improve future tailoring:\n")
    for gap in result.knowledge_gaps:
        print(f"  [{gap.severity}] {strip_em_dashes(gap.requirement)}")
        print(f"      {strip_em_dashes(gap.question)}\n")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("jd", nargs="?", type=Path,
                        help="A specific job description file. Defaults to every new file in job-descriptions/.")
    parser.add_argument("--force", action="store_true",
                        help="Re-tailor job descriptions that already have output.")
    args = parser.parse_args()

    api_key = load_api_key()
    if not api_key:
        print("ANTHROPIC_API_KEY is not set and no key was found in terraform.tfvars.", file=sys.stderr)
        return 1

    JD_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)

    if args.jd:
        if not args.jd.exists():
            print(f"No such job description: {args.jd}", file=sys.stderr)
            return 1
        jd_paths = [args.jd]
    else:
        jd_paths = sorted(
            p for p in JD_DIR.iterdir()
            if p.suffix.lower() in JD_SUFFIXES and p.name.lower() not in JD_IGNORED
        )
        if not args.force:
            jd_paths = [p for p in jd_paths if not (
                OUT_DIR / f"{p.stem}.md").exists()]

    if not jd_paths:
        print(
            f"Nothing to do. Drop a .md or .txt job description into {JD_DIR.relative_to(REPO_ROOT)}/ and run again.")
        print("Use --force to re-tailor job descriptions that already have output.")
        return 0

    knowledge_base = KNOWLEDGE_BASE.read_text(encoding="utf-8")
    try:
        resume_text = fetch_resume_text()
    except Exception as exc:
        print(
            f"Could not fetch the resume PDF from S3 ({exc}). Continuing with the knowledge base only.\n")
        resume_text = "(current resume unavailable — build the resume from the knowledge base)"

    client = anthropic.Anthropic(api_key=api_key)

    for jd_path in jd_paths:
        jd_text = jd_path.read_text(encoding="utf-8").strip()
        if not jd_text:
            print(f"{jd_path.name}: empty, skipping.")
            continue

        print(f"Tailoring for {jd_path.name}...")
        result = tailor(client, jd_text, resume_text, knowledge_base)

        out_path = OUT_DIR / f"{jd_path.stem}.md"
        out_path.write_text(render(result, jd_path), encoding="utf-8")

        print(
            f"  {result.role_title} at {result.company} | match: {result.match_strength}")
        print(f"  Wrote {out_path.relative_to(REPO_ROOT)}")
        report_gaps(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())
