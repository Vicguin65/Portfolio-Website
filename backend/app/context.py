import json
from io import BytesIO

import boto3
from pypdf import PdfReader

BUCKET = "whoistylerdu.com"
RESUME_KEY = "Resume_Tyler_Du.pdf"
KNOWLEDGE_BASE_KEY = "knowledge_base.md"
MEDIA_KEY = "media.json"


def fetch_s3_text(key: str) -> str:
    s3 = boto3.client("s3", region_name="us-west-1")
    obj = s3.get_object(Bucket=BUCKET, Key=key)
    return obj["Body"].read().decode("utf-8")


def fetch_resume_text() -> str:
    s3 = boto3.client("s3", region_name="us-west-1")
    obj = s3.get_object(Bucket=BUCKET, Key=RESUME_KEY)
    reader = PdfReader(BytesIO(obj["Body"].read()))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def fetch_knowledge_base() -> str:
    return fetch_s3_text(KNOWLEDGE_BASE_KEY)


def fetch_media_section() -> str:
    raw = fetch_s3_text(MEDIA_KEY)
    entries = json.loads(raw)
    lines = []
    for e in entries:
        lines.append(f"- {e['title']} ({e['publication']}, {e['date']})")
        lines.append(f"  {e['description']}")
        for link in e.get("links", []):
            lines.append(f"  {link['label']}: {link['url']}")
    return "\n".join(lines)
