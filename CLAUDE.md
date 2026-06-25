# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

```
portfolio-website/              React frontend (Vite)
  index.html                    Vite entry HTML (root level — not public/)
  vite.config.js                Vite config; excludes pdfjs-dist from pre-bundler
  .env.example                  Copy to .env.local and set VITE_API_URL for local dev
  src/
    index.jsx                   Router setup — all routes defined here
    index.css                   Design tokens (CSS custom properties) + global reset + shared utilities
    App.jsx / App.css           Landing page (full-viewport hero, floating CSS blob animations)
    components/
      NavBar.jsx/.css           Sticky navbar; blur-on-scroll; mobile hamburger; active-link state
      Footer.jsx/.css           LinkedIn, GitHub, Email links
      projects.js               Project data array + date utilities — ESM exports (no JSX, stays .js)
      media.js                  Media/features data array — ESM export ({ media }); no JSX, stays .js
    pages/
      HomePage.jsx/.css         About + skills grid
      ProjectPage.jsx/.css      Auto-sorted project card grid
      ResumePage.jsx + .module.css         PDF viewer (react-pdf) with zoom toggle; PDF sourced from S3
      ContactPage.jsx + .module.css        Contact form — POSTs to VITE_API_URL/api/contact
      AskTylerPage.jsx + .module.css       AI assistant — POSTs JD to /api/ask, typewriter animation, react-markdown render
      MediaPage.jsx/.css                   Press/features listing — date-sorted cards at /features
      MediaDetailPage.jsx + .module.css    Individual feature post at /features/:slug; supports links, images, YouTube/video embeds
      NotFoundPage.jsx/.css

backend/                        Python FastAPI backend
  app/
    main.py                     FastAPI app + CORS middleware
    schemas.py                  Pydantic models (ContactRequest, ContactResponse, AskRequest, AskResponse)
    routers/
      health.py                 GET /api/health
      contact.py                POST /api/contact — sends email via SES
      agent.py                  POST /api/ask — Claude-powered JD fit evaluation
  requirements.txt              fastapi, mangum, pydantic[email], uvicorn, anthropic, pypdf
  lambda_function.py            Mangum(app) Lambda entry point

infrastructure/
  terraform/                    All AWS infrastructure as code
    terraform.tfvars            Gitignored — contains anthropic_api_key
  scripts/
    deploy_frontend.sh          Build React + sync to S3 + CloudFront invalidation
                                Resume_Tyler_Du.pdf is excluded from --delete sync
```

## Commands

### Frontend (`portfolio-website/`)
```bash
npm run dev      # Dev server → localhost:5173
npm run build    # Production build → dist/
npm run preview  # Preview production build locally
npm install      # Install after pulling
```

### Backend (`backend/`)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload   # Dev server → localhost:8000
```

### Infrastructure (`infrastructure/terraform/`)
```bash
terraform init    # First time, or after provider changes
terraform plan
terraform apply   # Reads anthropic_api_key from terraform.tfvars (gitignored)
```

### Deploy
```bash
# Frontend only
VITE_API_URL=https://api.whoistylerdu.com bash infrastructure/scripts/deploy_frontend.sh

# Infrastructure changes
cd infrastructure/terraform && terraform apply
```

## Architecture

**Routing** — `react-router-dom` v6 with `createBrowserRouter`. All routes registered in `src/index.jsx`. Root path (`/`) is the landing page (`App.jsx`); inner pages under `/home`, `/projects`, `/features`, `/features/:slug`, `/resume`, `/contact`, `/ask`.

**Design system** — CSS custom properties in `src/index.css` (`:root`). Key tokens: `--font-display` (DM Serif Display), `--font-body` (Inter), `--accent` (#4F6EF7), `--bg` (#F8F9FE). Shared utility classes (`btn-primary`, `btn-secondary`, `section-label`, `page-wrapper`, `container`) live in `index.css` as globals.

**Page layout convention** — every inner page uses `<div className="page-wrapper">` with `<NavBar />` at top and `<Footer />` at bottom.

**Project data** — `src/components/projects.js` is the single source of truth for the portfolio. ESM exports (`export { projects, diff_text, date_string, same_date }`). Use named imports, not `require()`.

**Features / media data** — `src/components/media.js` is the single source of truth for press mentions and features. ESM exports (`export { media, asset }`). Each entry has: `slug` (URL-safe ID), `title`, `publication`, `date` (Date object), `description`, `tags` (string[]), `links` (`{ label, url }[]`), `images` (`{ src, alt, caption }[]`), `videos` (`{ type: 'youtube'|'url', id?, url?, title }[]`). List is auto-sorted newest-first in `MediaPage`. Invalid slugs redirect to `/features`. To add a new feature, append an entry to the array — no backend or deploy needed beyond a frontend redeploy.

**Media assets** — Images and other per-post assets live in S3 under `s3://whoistylerdu.com/media/{slug}/{filename}` (us-west-1), served via CloudFront at `https://whoistylerdu.com/media/{slug}/{filename}`. Use the `asset(slug, filename)` helper in `media.js` to build these URLs. To upload a new asset: `aws s3 cp photo.jpg s3://whoistylerdu.com/media/{slug}/photo.jpg --cache-control "max-age=86400" --region us-west-1`. The `media/*` prefix and `media.json` are excluded from `--delete` in `deploy_frontend.sh` so assets and data are never wiped on frontend deploys.

**media.json / agent sync** — `deploy_frontend.sh` runs `portfolio-website/scripts/export-media.mjs` post-build, which serializes `media.js` to `media.json` (slug, title, publication, date, description, tags, links — no image/video URLs) and uploads it to `s3://whoistylerdu.com/media.json` with `no-cache`. The Lambda fetches it at request time alongside the resume and knowledge base and injects it into the system prompt as a `== Press & Features ==` section. No manual `knowledge_base.md` edits are needed — adding an entry to `media.js` and deploying the frontend is sufficient. Lambda IAM policy (`s3_resume` in `modules/api/main.tf`) grants `s3:GetObject` on `media.json`.

**Resume PDF** — Not tracked in git. Lives at `s3://whoistylerdu.com/Resume_Tyler_Du.pdf` (us-west-1). The frontend loads it from `https://whoistylerdu.com/Resume_Tyler_Du.pdf` (CloudFront). The backend agent fetches it via boto3 at request time to extract text for the AI system prompt. `deploy_frontend.sh` excludes it from `--delete` syncs so it isn't wiped on deploy. To update: `aws s3 cp Resume_Tyler_Du.pdf s3://whoistylerdu.com/Resume_Tyler_Du.pdf --cache-control "max-age=86400" --region us-west-1`

**Resume page** — `react-pdf` v9. Worker initialized via `new URL('pdfjs-dist/build/pdf.worker.min.mjs', import.meta.url)`. `pdfjs-dist` excluded from Vite pre-bundler via `optimizeDeps.exclude`.

**Contact form** — POSTs to `${VITE_API_URL}/api/contact`. For local dev, set `VITE_API_URL=http://localhost:8000` in `.env.local`. CORS is configured in FastAPI middleware only (not API Gateway).

**Ask Tyler (AI agent)** — POSTs to `${VITE_API_URL}/api/ask` with `{ job_description }`. Backend fetches two files from S3 at request time: the resume PDF (`Resume_Tyler_Du.pdf`, extracted via pypdf) and a markdown knowledge base (`knowledge_base.md`). Both are injected into the system prompt, then `claude-sonnet-4-6` (max 1024 tokens) evaluates fit. Returns `{ response }`. Frontend renders with `react-markdown` and a typewriter animation (word-by-word at ~35ms/word). Errors are raised as `HTTPException` so CORS headers are always present. API key stored as Lambda env var `ANTHROPIC_API_KEY` (set via `terraform.tfvars`).

**Knowledge base** — `knowledge_base.md` at repo root is the single source of truth for Tyler's full professional history (education, work experience, projects with rich detail, skills with context, accomplishments with metrics). It is NOT built into the Lambda — it lives in S3 and is fetched at runtime, so updates take effect immediately with just an S3 upload. To update: `aws s3 cp knowledge_base.md s3://whoistylerdu.com/knowledge_base.md --region us-west-1`. The file is tracked in git (it contains no secrets) and excluded from the frontend `--delete` sync.

**Hosting** — Frontend: S3 bucket `whoistylerdu.com` (us-west-1) + CloudFront distribution `E23G2M0PQP2735`. Backend: Lambda `portfolio-api` (us-east-1) behind API Gateway at `api.whoistylerdu.com`.

## Infrastructure (AWS)

**Account**: 416469482962 | **Backend region**: us-east-1 | **Frontend S3 region**: us-west-1

**Terraform state**: `s3://rcos-terraform/portfolio/api/terraform.tfstate` with S3 native locking (`use_lockfile = true`, requires Terraform ≥ 1.10). The old DynamoDB lock table (`terraform_tf_lockid`) has been deleted.

**Do not import into Terraform**: CloudFront distribution `E23G2M0PQP2735` and existing ACM cert `1cda7e15-0ac8-4eee-87e2-2075ae84b41e` — managed manually, modifying them risks frontend downtime.

**Route53 zone**: `Z018519720Z0JNEXD5A5B` for `whoistylerdu.com`

**SES**: `tyleryeedu@gmail.com` verified as sending identity. Account is in sandbox — request production access in AWS console (SES → Account dashboard) before the contact form can receive messages from unverified senders.

**Lambda IAM policies**: CloudWatch logs (basic execution), `ses:SendEmail` (all resources), `s3:GetObject` on `Resume_Tyler_Du.pdf`, `knowledge_base.md`, and `media.json` in `whoistylerdu.com` bucket.

**Lambda env vars**: `SENDER_EMAIL`, `RECIPIENT_EMAIL`, `SES_REGION`, `ANTHROPIC_API_KEY`. The API key value lives in `infrastructure/terraform/terraform.tfvars` (gitignored).

**Lambda auto-rebuild**: `null_resource.lambda_build` in `main.tf` re-runs `pip install` and repackages whenever any `.py` file or `requirements.txt` changes. Requires `pip` on PATH and builds a manylinux2014_x86_64 compatible package.

## Phase 3+ (planned)

Enhancements to the "Ask Tyler" agent:
- **MCP server** — integrate with Google Drive to surface actual work samples and documents as grounding context
- **GitHub links** — surface relevant repository links as evidence in fit evaluations
- **Richer context** — more structured knowledge about Tyler's skills, experience timeline, and accomplishments beyond what's in the resume PDF
- **Conversational follow-up** — allow recruiters to ask follow-up questions in a chat interface
