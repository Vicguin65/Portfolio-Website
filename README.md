# whoistylerdu.com

Personal portfolio website for Tyler Du — software engineer, curious mind.

![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-AWS-623CE4?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Lambda%20%7C%20CloudFront%20%7C%20SES-FF9900?logo=amazon-aws&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-Sonnet_4.6-D97706?logo=anthropic&logoColor=white)

## Stack

| Layer | Tech |
|---|---|
| Frontend | React 18 + Vite, React Router v6, react-markdown, CSS custom properties |
| Backend | Python 3.12, FastAPI, Mangum (Lambda adapter) |
| AI | Anthropic Claude Sonnet 4.6 — JD fit evaluation via `/api/ask` |
| Infrastructure | AWS Lambda, API Gateway, S3, CloudFront, SES, Route53, ACM |
| IaC | Terraform (state in S3, native S3 locking) |

## Local Development

**Frontend**
```bash
cd portfolio-website
cp .env.example .env.local   # set VITE_API_URL=http://localhost:8000
npm install
npm run dev                  # → localhost:5173
```

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload  # → localhost:8000
```

## Deploy

**Infrastructure** (run once, or on infra changes)
```bash
cd infrastructure/terraform
terraform init
terraform apply               # requires terraform.tfvars with anthropic_api_key
```

**Frontend**
```bash
VITE_API_URL=https://api.whoistylerdu.com \
  bash infrastructure/scripts/deploy_frontend.sh
```

Or use the `/deploy` and `/deploy-infra` slash commands in Claude Code.

> **Note:** `Resume_Tyler_Du.pdf` is not tracked in git. It lives at `s3://whoistylerdu.com/Resume_Tyler_Du.pdf` and is excluded from the frontend sync. To update it: `aws s3 cp Resume_Tyler_Du.pdf s3://whoistylerdu.com/Resume_Tyler_Du.pdf --cache-control "max-age=86400" --region us-west-1`

## Architecture

```
whoistylerdu.com  →  CloudFront  →  S3 (React build, us-west-1)
api.whoistylerdu.com  →  API Gateway  →  Lambda (FastAPI)  →  SES / Anthropic API
                                                            →  S3 (resume PDF read)
```

Routes: `/api/health` · `/api/contact` · `/api/ask`

## Ask Tyler (AI)

The `/ask` page lets recruiters paste a job description and get a Claude-powered evaluation of Tyler's fit. The agent is grounded in:
- Resume PDF fetched live from S3
- Project data from `src/components/projects.js`

Planned enhancements:
- MCP server integration with Google Drive (work samples)
- GitHub repository links surfaced as evidence
- Richer conversational context

## Roadmap

- [x] Phase 1 — UI overhaul (light + dreamy theme, Vite migration)
- [x] Phase 2 — FastAPI backend + AWS infrastructure via Terraform
- [x] Phase 3 — Agentic AI: Claude-powered recruiter assistant (`/ask`)
- [ ] Phase 3+ — MCP server (Google Drive, GitHub), richer agent context
