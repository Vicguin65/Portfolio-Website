import logging
import os
from io import BytesIO

import anthropic
import boto3
from fastapi import APIRouter, HTTPException
from pypdf import PdfReader

from app.schemas import AskRequest, AskResponse

logger = logging.getLogger(__name__)

router = APIRouter()

RESUME_BUCKET = "whoistylerdu.com"
RESUME_KEY = "Resume_Tyler_Du.pdf"

# Serialized from projects.js — single source of truth kept in sync manually
PROJECTS_CONTEXT = """\
- "Who is Tyler Du" (Sep 2024–present): Personal portfolio website. Stack: React, FastAPI, AWS Lambda, CloudFront, Terraform
- Dandy's World Discord Bot (Oct 2024, built in 3 days): Automates party/channel creation via slash commands. Stack: Python discord.py, AWS EC2
- Accessible Routes (Sep 2023–Nov 2024): Campus accessibility routing API using RPI building data. Stack: React, Django, CSS, AWS EC2
- REST API For AWS Identity Store (Jan–May 2024): Open-source collaboration with IBM's cloud team. Stack: Python, AWS Lambda, AWS CloudFormation
- Terraform Automation For Data Science App (May–Aug 2024): Automated AWS VPC with 4 Ubuntu servers hosting a data science app. Stack: HCP Terraform CDK, AWS VPC, React
- Grouping API for Camp Students (Jan–Apr 2023): Django REST API + PostgreSQL grouping algorithm matching 300 students by survey similarity. Stack: Python, Django, PostgreSQL
- Hiring Management System Automation (May–Aug 2022): Lever API automation saving 100+ hrs/hiring season; scikit-learn resume classifier with 88% accuracy trained on 1,700 candidate records. Stack: Python, Scikit-Learn, AWS S3
- School Contacts Webscrape (Jun–Jul 2023): Scraped 68,000+ faculty records. Stack: Python, BeautifulSoup4, Selenium, GPT-3.5-turbo\
"""

SYSTEM_PROMPT_TEMPLATE = """\
You are an assistant that evaluates how well Tyler Du — a software engineer and RPI CS graduate — fits a given job description. Use his resume and project history as your primary sources.

== Resume ==
{resume_text}

== Projects ==
{projects}

Structure your response exactly like this (use the bold headers as written):

**Role Summary**
2-3 sentences describing what the role is looking for.

**Fit Assessment**
One of: Strong Fit | Good Fit | Partial Fit — followed by 1-2 sentences of honest reasoning. Acknowledge gaps if they exist.

**Most Relevant Experience**
3-5 bullet points. Each names a specific project or experience and explains in one sentence why it matters for this role.

**Interview Talking Points**
2-3 bullet points Tyler should emphasize for this specific role.

Be concise, specific, and honest.\
"""


def _fetch_resume_text() -> str:
    s3 = boto3.client("s3", region_name="us-west-1")
    obj = s3.get_object(Bucket=RESUME_BUCKET, Key=RESUME_KEY)
    reader = PdfReader(BytesIO(obj["Body"].read()))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


@router.post("/ask", response_model=AskResponse)
async def ask_tyler(request: AskRequest):
    try:
        resume_text = _fetch_resume_text()
    except Exception:
        resume_text = "(resume unavailable — using projects list only)"

    system = SYSTEM_PROMPT_TEMPLATE.format(
        resume_text=resume_text,
        projects=PROJECTS_CONTEXT,
    )

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            messages=[{"role": "user", "content": f"Job Description:\n\n{request.job_description}"}],
        )
    except anthropic.APIError as exc:
        logger.error("Anthropic API error: %s", exc)
        raise HTTPException(status_code=502, detail="AI service unavailable. Please try again later.")

    return AskResponse(response=message.content[0].text)
