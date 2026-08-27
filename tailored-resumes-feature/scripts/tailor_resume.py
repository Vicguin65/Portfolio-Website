#!/usr/bin/env python3
"""Tailor Tyler's resume to a job description using Claude.

Drop a job description into job-descriptions/ and run this script. For each one it
writes a tailored resume to tailored-resumes/ as both Markdown and a PDF matching
the standing resume, plus any requirement the knowledge base cannot support.

Run from the repo root:

    python tailored-resumes-feature/scripts/tailor_resume.py
    python tailored-resumes-feature/scripts/tailor_resume.py --force
    python tailored-resumes-feature/scripts/tailor_resume.py path/to/jd.md
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Literal

import anthropic
from pydantic import BaseModel, Field, ValidationError

FEATURE_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = FEATURE_ROOT.parent
sys.path.insert(0, str(REPO_ROOT / "backend"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.context import fetch_resume_text  # noqa: E402
from resume_pdf import overflow_lines, write_pdf  # noqa: E402

JD_DIR = FEATURE_ROOT / "job-descriptions"
OUT_DIR = FEATURE_ROOT / "tailored-resumes"
KNOWLEDGE_BASE = REPO_ROOT / "knowledge_base.md"
TFVARS = REPO_ROOT / "infrastructure" / "terraform" / "terraform.tfvars"

MODEL = "claude-opus-5"
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


class ResumeHeader(BaseModel):
    name: str = Field(description="Tyler's full name, exactly as it appears on the current resume. Never empty.")
    contact_lines: list[str] = Field(
        description="The contact lines under the name, copied from the current resume. Normally two: location/email/site, then the profile links.",
    )


class ResumeEntry(BaseModel):
    title: str = Field(
        description="Bold left-hand text. For jobs, the employer. For projects, the project line. For education, the school."
    )
    location: str = Field(
        description="Right-aligned text on the title line, usually a city and state. Empty string when the title line should run full width."
    )
    subtitle: str = Field(
        description="Italic left-hand text on the second line, usually the role held. Empty string if there is none."
    )
    dates: str = Field(
        description="Italic right-aligned dates on the second line, e.g. 'July 2025 - Present'. Empty string if there are none."
    )
    bullets: list[str] = Field(
        description="Accomplishment bullets. Wrap key technologies and metrics in **double asterisks** to bold them, matching the current resume."
    )


class ResumeSection(BaseModel):
    heading: str = Field(description="Section heading in capitals, e.g. 'WORK EXPERIENCE', 'PROJECTS', 'SKILLS & AWARDS', 'EDUCATION'.")
    lines: list[str] = Field(
        description="Full-width lines for list-style sections like skills, e.g. '**Languages:** Python, Java, ...'. Empty list for sections that use entries."
    )
    entries: list[ResumeEntry] = Field(
        description="Entries for sections like work experience, projects, and education. Empty list for sections that use lines."
    )


class TailoredResume(BaseModel):
    role_title: str = Field(description="The job title this resume is tailored for.")
    company: str = Field(description="The hiring company, or 'Unknown' if the description does not name one.")
    match_strength: Literal["Strong", "Good", "Partial", "Weak"]
    match_reasoning: str = Field(description="Two or three sentences of honest reasoning about the fit, gaps included.")
    header: ResumeHeader
    sections: list[ResumeSection] = Field(
        description="The complete resume body, in the order it should appear. Most relevant section for this role first. Always populate this fully, however weak the match is.",
    )
    tailoring_notes: list[str] = Field(
        description="What was emphasized, reordered, or cut for this role, and why. One line each.",
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

4. Match the structure of the current resume. Keep the same header, the same section \
headings in capitals (WORK EXPERIENCE, PROJECTS, SKILLS & AWARDS, EDUCATION), the same \
employer/location then role/dates two-line entry pattern, and the same bullet voice: \
start with a past-tense verb, no trailing period unless the bullet is a full sentence. \
Reorder sections and entries so the most relevant material for this role comes first, and \
drop material that does not serve this application.

5. It must fit on ONE page. The page holds about 46 lines in total, and section headings \
and the spacing around entries consume roughly 12 of them, so you have about 34 lines of \
actual content. A bullet wraps to a new line every ~105 characters, so a 210 character \
bullet costs 2 lines and a 315 character bullet costs 3. Each entry costs 2 lines before \
its bullets. Add up your budget before you write, and cut aggressively rather than \
overflow: 3 or 4 entries with 2 to 4 bullets each, plus a short skills block, is typical.

6. Bold sparingly and deliberately. Wrap only the key technologies and the hard numbers in \
**double asterisks**, the way the current resume does. Never bold a whole bullet.

7. Placeholders marked [TODO: ...] in the knowledge base are unanswered questions, not \
facts. Never treat their content as real experience. If a TODO sits on something this \
role needs, that is a knowledge gap.

8. Be honest in match_strength and match_reasoning. A recruiter reading an inflated \
assessment is worse off than one reading an accurate one.

9. Knowledge gaps are the most valuable thing you produce. When the role needs something \
the sources do not cover, write a question specific enough that Tyler's answer could be \
pasted straight into the knowledge base. "Have you used Kubernetes?" is a bad question. \
"Have you deployed or operated anything on Kubernetes, and if so, what was running on it \
and roughly what scale?" is a good one. If Tyler genuinely has relevant experience for \
every requirement, return an empty list rather than manufacturing concerns.

10. Never use em dashes (the character) anywhere in your output. Use commas, periods, \
colons, or parentheses instead. This applies to the resume and to every other field.

11. Always return a complete resume, no matter how weak the match is. A weak match means \
an honest match_strength and a long list of knowledge gaps, never an empty header or an \
empty sections list. Tyler still needs a resume to send.\
"""


def load_api_key() -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    if TFVARS.exists():
        match = re.search(
            r'^\s*anthropic_api_key\s*=\s*"([^"]+)"', TFVARS.read_text(encoding="utf-8"), re.MULTILINE
        )
        if match:
            return match.group(1)
    return None


class TailoringError(RuntimeError):
    pass


def _check(resume: TailoredResume) -> TailoredResume:
    """The model occasionally returns an empty body. Catch that before it reaches a PDF.

    These are deliberately checked here rather than as pydantic constraints on the model:
    the SDK validates the parsed response inside the stream, so a constraint violation
    would raise there and escape the retry loop below.
    """
    if not resume.header.name.strip():
        raise TailoringError("model returned an empty name")
    if not resume.header.contact_lines:
        raise TailoringError("model returned no contact lines")
    if len(resume.sections) < 2:
        raise TailoringError(f"model returned only {len(resume.sections)} section(s)")
    body = sum(len(s.entries) + len(s.lines) for s in resume.sections)
    if body < 3:
        raise TailoringError(f"model returned an almost empty resume ({body} entries across {len(resume.sections)} sections)")
    return resume


TRIM_INSTRUCTION = """\

Your previous draft ran about {n} lines past the bottom of a single page. Produce the \
same resume about {n} lines shorter. Cut the least relevant bullets first, then the least \
relevant entry, then the least relevant section. Keep the header intact and keep every \
bullet you retain fully intact: shorten by removing material, not by truncating sentences.\
"""

MAX_ATTEMPTS = 3


def tailor(client: anthropic.Anthropic, jd_text: str, resume_text: str, knowledge_base: str) -> TailoredResume:
    system = SYSTEM_PROMPT.format(resume_text=resume_text, knowledge_base=knowledge_base)
    base_prompt = f"Job Description:\n\n{jd_text}"
    prompt = base_prompt
    last_error = None
    best = None
    best_over = None

    for attempt in range(MAX_ATTEMPTS):
        try:
            with client.messages.stream(
                model=MODEL,
                max_tokens=32000,
                system=system,
                thinking={"type": "adaptive"},
                output_config={"effort": "high"},
                output_format=TailoredResume,
                messages=[{"role": "user", "content": prompt}],
            ) as stream:
                message = stream.get_final_message()
        except ValidationError as exc:
            last_error = TailoringError(f"model returned a response that did not fit the schema ({exc.error_count()} error(s))")
            print(f"  {last_error}. Retrying.")
            prompt = base_prompt
            continue

        if message.stop_reason == "max_tokens":
            raise TailoringError("response hit max_tokens before finishing; raise max_tokens and retry")

        try:
            result = _check(message.parsed_output)
        except TailoringError as exc:
            last_error = exc
            print(f"  Incomplete response ({exc}). Retrying.")
            prompt = base_prompt
            continue

        over = overflow_lines(result)
        if not over:
            return result

        if best_over is None or over < best_over:
            best, best_over = result, over
        last_error = TailoringError(f"resume runs {best_over} line(s) past one page")
        if attempt < MAX_ATTEMPTS - 1:
            print(f"  Runs {over} line(s) past one page. Asking for a tighter draft.")
        prompt = base_prompt + TRIM_INSTRUCTION.format(n=over + 1)

    if best is not None:
        print(f"  Warning: {last_error}. Keeping the tightest draft.")
        return best
    raise TailoringError(str(last_error))


def strip_em_dashes(text: str) -> str:
    """Em dashes are banned in this project's text. Pipes suit list-style lines, commas suit prose."""
    return "\n".join(
        line.replace(" — ", " | " if " | " in line else ", ").replace("—", ",")
        for line in text.splitlines()
    )


def sanitize(resume: TailoredResume) -> TailoredResume:
    resume = resume.model_copy(deep=True)
    resume.match_reasoning = strip_em_dashes(resume.match_reasoning)
    resume.header.contact_lines = [strip_em_dashes(c) for c in resume.header.contact_lines]
    resume.tailoring_notes = [strip_em_dashes(n) for n in resume.tailoring_notes]
    for gap in resume.knowledge_gaps:
        gap.requirement = strip_em_dashes(gap.requirement)
        gap.question = strip_em_dashes(gap.question)
    for section in resume.sections:
        section.lines = [strip_em_dashes(line) for line in section.lines]
        for entry in section.entries:
            entry.title = strip_em_dashes(entry.title)
            entry.subtitle = strip_em_dashes(entry.subtitle)
            entry.location = strip_em_dashes(entry.location)
            entry.dates = strip_em_dashes(entry.dates)
            entry.bullets = [strip_em_dashes(b) for b in entry.bullets]
    return resume


def render_markdown(result: TailoredResume, jd_path: Path) -> str:
    title = result.role_title
    if result.company.lower() not in title.lower():
        title = f"{title} at {result.company}"

    lines = [
        f"<!-- company: {result.company} -->",
        "",
        f"# {title}",
        "",
        f"*Tailored from `{jd_path.name}` | Match: **{result.match_strength}***",
        "",
        result.match_reasoning,
        "",
        "---",
        "",
        f"## {result.header.name}",
        "",
    ]
    lines += [f"{line}  " for line in result.header.contact_lines]

    for section in result.sections:
        lines += ["", f"### {section.heading}", ""]
        for line in section.lines:
            lines += [line, ""]
        for entry in section.entries:
            head = f"**{entry.title}**"
            if entry.location:
                head += f" | {entry.location}"
            lines.append(head)
            if entry.subtitle or entry.dates:
                sub = " | ".join(p for p in (entry.subtitle, entry.dates) if p)
                lines.append(f"*{sub}*")
            lines.append("")
            lines += [f"- {b}" for b in entry.bullets]
            lines.append("")

    lines += ["---", "", "## Tailoring Notes", ""]
    lines += [f"- {note}" for note in result.tailoring_notes]

    lines += ["", "## Knowledge Base Gaps", ""]
    if result.knowledge_gaps:
        lines.append(
            "The knowledge base has no evidence for the following. Answer these and add "
            "them to `knowledge_base.md` so future tailoring can draw on them."
        )
        lines.append("")
        for gap in result.knowledge_gaps:
            lines += [f"### {gap.requirement}  `{gap.severity}`", "", gap.question, ""]
    else:
        lines.append("None. The knowledge base covers this role.")

    return "\n".join(lines) + "\n"


def slug(text: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    return cleaned or "Role"


def report_gaps(result: TailoredResume) -> None:
    if not result.knowledge_gaps:
        print("  No knowledge base gaps for this role.")
        return

    print(f"  {len(result.knowledge_gaps)} knowledge base gap(s). Answer these to improve future tailoring:\n")
    for gap in result.knowledge_gaps:
        print(f"  [{gap.severity}] {gap.requirement}")
        print(f"      {gap.question}\n")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("jd", nargs="?", type=Path, help="A specific job description file. Defaults to every new file in job-descriptions/.")
    parser.add_argument("--force", action="store_true", help="Re-tailor job descriptions that already have output.")
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
            jd_paths = [p for p in jd_paths if not (OUT_DIR / f"{p.stem}.md").exists()]

    if not jd_paths:
        print(f"Nothing to do. Drop a .md or .txt job description into {JD_DIR.relative_to(REPO_ROOT)}/ and run again.")
        print("Use --force to re-tailor job descriptions that already have output.")
        return 0

    knowledge_base = KNOWLEDGE_BASE.read_text(encoding="utf-8")
    try:
        resume_text = fetch_resume_text()
    except Exception as exc:
        print(f"Could not fetch the resume PDF from S3 ({exc}). Continuing with the knowledge base only.\n")
        resume_text = "(current resume unavailable, build the resume from the knowledge base)"

    client = anthropic.Anthropic(api_key=api_key)
    failures = 0

    for jd_path in jd_paths:
        jd_text = jd_path.read_text(encoding="utf-8").strip()
        if not jd_text:
            print(f"{jd_path.name}: empty, skipping.")
            continue

        print(f"Tailoring for {jd_path.name}...")
        try:
            result = sanitize(tailor(client, jd_text, resume_text, knowledge_base))
        except (TailoringError, anthropic.APIError) as exc:
            print(f"  Failed: {exc}\n", file=sys.stderr)
            failures += 1
            continue

        md_path = OUT_DIR / f"{jd_path.stem}.md"
        md_path.write_text(render_markdown(result, jd_path), encoding="utf-8")

        company = result.company if result.company.lower() != "unknown" else jd_path.stem
        pdf_path = OUT_DIR / f"Du_Tyler_Resume_{slug(company)}.pdf"
        write_pdf(result, pdf_path, title=f"{result.header.name} Resume, {result.company}")

        print(f"  {result.role_title} at {result.company} | match: {result.match_strength}")
        print(f"  Wrote {md_path.relative_to(REPO_ROOT)}")
        print(f"  Wrote {pdf_path.relative_to(REPO_ROOT)}")
        report_gaps(result)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
