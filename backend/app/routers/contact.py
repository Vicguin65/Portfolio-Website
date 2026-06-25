import os
import logging

import boto3
from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException

from app.schemas import ContactRequest, ContactResponse

logger = logging.getLogger(__name__)
router = APIRouter()

SENDER_EMAIL    = os.environ.get("SENDER_EMAIL",    "tyleryeedu@gmail.com")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", "tyleryeedu@gmail.com")
SES_REGION      = os.environ.get("SES_REGION",      "us-east-1")


@router.post("/contact", response_model=ContactResponse)
async def contact(request: ContactRequest):
    ses = boto3.client("ses", region_name=SES_REGION)

    subject = f"Portfolio contact from {request.name}"
    body_text = (
        f"Name:    {request.name}\n"
        f"Email:   {request.email}\n"
        f"\nMessage:\n{request.message}"
    )

    try:
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={"ToAddresses": [RECIPIENT_EMAIL]},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body":    {"Text": {"Data": body_text, "Charset": "UTF-8"}},
            },
            ReplyToAddresses=[request.email],
        )
    except ClientError as exc:
        logger.error("SES send_email failed: %s", exc.response["Error"])
        raise HTTPException(status_code=500, detail="Failed to send message.")

    return ContactResponse(success=True, message="Message sent successfully.")
