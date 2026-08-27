# Tailored Resumes

Drop a job description in, get back a resume tailored to it: as Markdown you can edit,
and as a one-page PDF formatted like the standing resume.

```
tailored-resumes-feature/
  job-descriptions/     Drop a .md or .txt job description here
  tailored-resumes/     Output: <jd-name>.md and Du_Tyler_Resume_<Company>.pdf
  scripts/
    tailor_resume.py    Calls Claude, writes the Markdown and the PDF
    render_resume.py    Rebuilds a PDF from a hand-edited Markdown file
    resume_pdf.py       The PDF renderer (layout matched to Du_Tyler_Resume.pdf)
  requirements.txt      Local tooling deps; the Lambda does not install these
```

## Setup

```bash
pip install -r tailored-resumes-feature/requirements.txt
```

The Anthropic API key comes from `ANTHROPIC_API_KEY`, falling back to `anthropic_api_key`
in `infrastructure/terraform/terraform.tfvars`.

## Usage

All commands run from the repo root.

```bash
# 1. Drop a job description into job-descriptions/ as .md or .txt

# 2. Tailor every job description that has no output yet
python tailored-resumes-feature/scripts/tailor_resume.py

python tailored-resumes-feature/scripts/tailor_resume.py --force        # re-tailor all
python tailored-resumes-feature/scripts/tailor_resume.py path/to/jd.md  # just one

# 3. Optionally edit tailored-resumes/<jd-name>.md, then rebuild its PDF
python tailored-resumes-feature/scripts/render_resume.py                # every .md
python tailored-resumes-feature/scripts/render_resume.py salesforce.md  # just one
```

A bare filename passed to `render_resume.py` resolves inside `tailored-resumes/`.

## What it does

Grounding comes from `knowledge_base.md` at the repo root plus the resume PDF fetched
from S3. The model is instructed never to claim anything those sources do not support:
if a role asks for something Tyler has not done, it goes in the gaps list instead of the
resume.

Each run writes two files:

- `<jd-name>.md`, the resume plus tailoring notes and a **Knowledge Base Gaps** section
- `Du_Tyler_Resume_<Company>.pdf`, the resume alone, held to one page

Answering the gap questions in `knowledge_base.md` (then `aws s3 cp`-ing it up) improves
both this tool and the Ask Tyler agent on the site.

## Editing before you send

The Markdown is the editable surface. Change the resume body, which is everything between
the first `---` and the `## Tailoring Notes` heading, then run `render_resume.py` on it.
An unedited file re-renders to an identical PDF, so editing is safe.

| Markdown | Becomes |
|---|---|
| `## Tyler Du` + following lines | name and contact block |
| `### WORK EXPERIENCE` | a section heading with its rule |
| `**Employer** \| Location` | bold line, location right-aligned |
| `*Role \| Dates*` | italic line, dates right-aligned |
| `- text` | a bullet |
| `**Languages:** Python, ...` | a full-width line (skills-style sections) |
| `**bold**` inside a bullet | bold text |

Reordering and deleting work too. Notes and gaps below the resume are ignored. The
renderer warns if an edit pushes the resume past one page.
