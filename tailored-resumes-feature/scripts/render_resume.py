#!/usr/bin/env python3
"""Rebuild a resume PDF from an edited Markdown file.

Edit a resume in tailored-resumes/, then run this to regenerate its
Du_Tyler_Resume_<Company>.pdf. Only the resume body is read; the tailoring notes
and knowledge base gaps below it are ignored.

Run from the repo root (a bare filename resolves inside tailored-resumes/):

    python tailored-resumes-feature/scripts/render_resume.py
    python tailored-resumes-feature/scripts/render_resume.py salesforce.md
    python tailored-resumes-feature/scripts/render_resume.py salesforce.md -o /tmp/out.pdf
"""

import argparse
import re
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))

from resume_pdf import overflow_lines, write_pdf  # noqa: E402
from tailor_resume import OUT_DIR, ResumeEntry, ResumeHeader, ResumeSection, slug  # noqa: E402

COMPANY_RE = re.compile(r"<!--\s*company:\s*(.+?)\s*-->", re.IGNORECASE)
ENTRY_RE = re.compile(r"^\*\*(.+?)\*\*\s*(?:\|\s*(.+))?$")
SUBTITLE_RE = re.compile(r"^\*(?!\*)(.+?)\*$")
BULLET_RE = re.compile(r"^[-*]\s+(.*)$")
HEADING_RE = re.compile(r"^###\s+(.*)$")
NAME_RE = re.compile(r"^##\s+(.*)$")


class ParseError(ValueError):
    pass


def _resume_body(text: str) -> list[str]:
    """The resume lives between the first '---' and the '## Tailoring Notes' section."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "---") + 1
    except StopIteration:
        raise ParseError("no '---' separator found before the resume")

    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].strip().lower().startswith(("## tailoring notes", "## knowledge base gaps")):
            end = i
            break

    while end > start and lines[end - 1].strip() in ("", "---"):
        end -= 1
    return lines[start:end]


def parse_markdown(text: str):
    """Turn a rendered resume Markdown file back into header and section objects."""
    body = _resume_body(text)

    name = None
    contact: list[str] = []
    sections: list[ResumeSection] = []
    section = None
    entry = None

    def close_entry():
        nonlocal entry
        if entry is not None:
            section.entries.append(ResumeEntry(**entry))
            entry = None

    for raw in body:
        line = raw.strip()
        if not line:
            continue

        heading = HEADING_RE.match(line)
        if heading:
            close_entry()
            section = ResumeSection(heading=heading.group(1).strip(), lines=[], entries=[])
            sections.append(section)
            continue

        if section is None:
            title = NAME_RE.match(line)
            if title:
                name = title.group(1).strip()
            elif name:
                contact.append(line.rstrip("\\").strip())
            continue

        bullet = BULLET_RE.match(line)
        if bullet:
            if entry is None:
                raise ParseError(f"bullet with no entry above it: {line!r}")
            entry["bullets"].append(bullet.group(1).strip())
            continue

        subtitle = SUBTITLE_RE.match(line)
        if subtitle and entry is not None and not entry["subtitle"] and not entry["bullets"]:
            left, _, right = subtitle.group(1).rpartition(" | ")
            entry["subtitle"], entry["dates"] = (left.strip(), right.strip()) if left else (right.strip(), "")
            continue

        head = ENTRY_RE.match(line)
        if head:
            close_entry()
            entry = {
                "title": head.group(1).strip(),
                "location": (head.group(2) or "").strip(),
                "subtitle": "",
                "dates": "",
                "bullets": [],
            }
            continue

        section.lines.append(line)

    close_entry()

    if not name:
        raise ParseError("no '## Name' heading found in the resume body")
    if not sections:
        raise ParseError("no '### SECTION' headings found in the resume body")

    return SimpleNamespace(
        header=ResumeHeader(name=name, contact_lines=contact),
        sections=sections,
    )


def company_of(text: str, md_path: Path) -> str:
    """Prefer the metadata comment, fall back to the '# Role at Company' title."""
    match = COMPANY_RE.search(text)
    if match:
        return match.group(1)
    for line in text.splitlines():
        if line.startswith("# ") and " at " in line:
            return line[2:].rsplit(" at ", 1)[1].strip()
    return md_path.stem


def render(md_path: Path, out_path: Path | None) -> int:
    text = md_path.read_text(encoding="utf-8")
    resume = parse_markdown(text)

    if out_path is None:
        out_path = md_path.parent / f"Du_Tyler_Resume_{slug(company_of(text, md_path))}.pdf"

    write_pdf(resume, out_path, title=f"{resume.header.name} Resume")

    entries = sum(len(s.entries) for s in resume.sections)
    bullets = sum(len(e.bullets) for s in resume.sections for e in s.entries)
    print(f"  {len(resume.sections)} sections, {entries} entries, {bullets} bullets")
    print(f"  Wrote {out_path}")

    over = overflow_lines(resume)
    if over:
        print(f"  Warning: runs {over} line(s) past one page. Trim a bullet and run again.")
    return over


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("markdown", nargs="?", type=Path, help="An edited resume Markdown file. Defaults to every .md in tailored-resumes/.")
    parser.add_argument("-o", "--output", type=Path, help="Write the PDF here instead of the default name.")
    args = parser.parse_args()

    if args.markdown:
        path = args.markdown if args.markdown.exists() else OUT_DIR / args.markdown.name
        if not path.exists():
            print(f"No such file: {args.markdown}", file=sys.stderr)
            return 1
        paths = [path]
    elif args.output:
        print("--output needs a single Markdown file.", file=sys.stderr)
        return 1
    else:
        paths = sorted(OUT_DIR.glob("*.md"))

    if not paths:
        print(f"No Markdown files in {OUT_DIR}.")
        return 0

    failures = 0
    overflowed = 0
    for path in paths:
        print(f"Rendering {path.name}...")
        try:
            overflowed += bool(render(path, args.output))
        except (ParseError, ValueError) as exc:
            print(f"  Failed: {exc}\n", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
