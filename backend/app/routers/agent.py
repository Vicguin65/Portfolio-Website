import logging
import os

import anthropic
from fastapi import APIRouter, HTTPException

from app.context import fetch_knowledge_base, fetch_media_section, fetch_resume_text
from app.schemas import AskRequest, AskResponse

logger = logging.getLogger(__name__)

router = APIRouter()

SYSTEM_PROMPT_TEMPLATE = """\
You are an assistant that evaluates how well Tyler Du — a software engineer and RPI CS graduate — fits a given job description. Use his resume, knowledge base, and press features as your primary sources.

== Resume ==
{resume_text}

== Professional Knowledge Base ==
{knowledge_base}

== Press & Features ==
{media_section}

Structure your response exactly like this (use the bold headers as written):

**Role Summary**
2-3 sentences describing what the role is looking for.

**Fit Assessment**
One of: Strong Fit | Good Fit | Partial Fit — followed by 1-2 sentences of honest reasoning. Acknowledge gaps if they exist.

**Most Relevant Experience**
3-5 bullet points. Each names a specific project or experience, explains in one sentence why it matters for this role, and includes the GitHub link if one is available (e.g. "Code: https://github.com/...").

**Interview Talking Points**
2-3 bullet points Tyler should emphasize for this specific role.

Be concise, specific, and honest.\
"""


@router.post("/ask", response_model=AskResponse)
async def ask_tyler(request: AskRequest):
    try:
        resume_text = fetch_resume_text()
    except Exception:
        logger.warning("Could not fetch resume PDF from S3")
        resume_text = "(resume unavailable)"

    try:
        knowledge_base = fetch_knowledge_base()
    except Exception:
        logger.warning("Could not fetch knowledge base from S3")
        knowledge_base = "(knowledge base unavailable)"

    try:
        media_section = fetch_media_section()
    except Exception:
        logger.warning("Could not fetch media.json from S3")
        media_section = "(press features unavailable)"

    system = SYSTEM_PROMPT_TEMPLATE.format(
        resume_text=resume_text,
        knowledge_base=knowledge_base,
        media_section=media_section,
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
