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
    ats.py              Keyword extraction and coverage scoring, and a standalone audit
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

# 4. Audit any resume against a description's keywords, without calling the API
python tailored-resumes-feature/scripts/ats.py salesforce
python tailored-resumes-feature/scripts/ats.py salesforce --all
```

A bare filename passed to `render_resume.py` resolves inside `tailored-resumes/`.

## What it does

Grounding comes from `knowledge_base.md` at the repo root plus the resume PDF fetched
from S3. The model is instructed never to claim anything those sources do not support:
if a role asks for something Tyler has not done, it goes in the gaps list instead of the
resume.

Each run writes two files:

- `<jd-name>.md`, the resume plus tailoring notes, a **Knowledge Base Gaps** section, and
  an **ATS Keyword Coverage** section
- `Du_Tyler_Resume_<Company>.pdf`, the resume alone, held to one page

Answering the gap questions in `knowledge_base.md` (then `aws s3 cp`-ing it up) improves
both this tool and the Ask Tyler agent on the site.

## ATS keywords

Most resumes are filtered by software before a person reads them, and that software does
not read: it looks for the description's own words. `ats.py` models it. It pulls the terms
out of a description, tiers them by how hard the description leans on each one, and checks
which ones a resume actually contains.

Tailoring uses this in two places. The ranked list goes into the prompt, so the model
phrases real experience in the description's vocabulary: drift correction becomes
monitoring when that is the word the job uses. Then every draft is scored, and a draft
that misses a critical term gets sent back, in the same retry loop that fixes page
overflow. Fitting on one page still wins over a keyword.

The honesty rule does not bend for keywords. A term the knowledge base cannot support
stays off the resume and turns into a gap question instead: a keyword that gets you a
phone screen you cannot survive is worse than a miss.

Run it on its own to audit a resume you already have, including the untailored base:

```bash
python tailored-resumes-feature/scripts/ats.py solace --resume Du_Tyler_Resume_Base.pdf
```

It also flags knockouts, the rules that reject a resume before any keyword is scored: a
missing phone number, no work authorization line where the description raises it, and a
location outside the radius of an onsite role.

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
