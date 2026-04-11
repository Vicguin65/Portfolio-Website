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
    pages/
      HomePage.jsx/.css         About + skills grid
      ProjectPage.jsx/.css      Auto-sorted project card grid
      ResumePage.jsx + .module.css    PDF viewer (react-pdf) with zoom toggle
      ContactPage.jsx + .module.css   Contact form — POSTs to VITE_API_URL/api/contact
      NotFoundPage.jsx/.css

backend/                        Python FastAPI backend
  app/
    main.py                     FastAPI app + CORS middleware
    schemas.py                  Pydantic models (ContactRequest, ContactResponse)
    routers/
      health.py                 GET /api/health
      contact.py                POST /api/contact — sends email via SES
  requirements.txt              fastapi, mangum, pydantic[email], uvicorn
  lambda_function.py            Mangum(app) Lambda entry point

infrastructure/
  terraform/                    All AWS infrastructure as code
  scripts/
    deploy_frontend.sh          Build React + sync to S3 + CloudFront invalidation
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
terraform apply
```

### Deploy
```bash
# Frontend only
VITE_API_URL=https://api.whoistylerdu.com bash infrastructure/scripts/deploy_frontend.sh

# Infrastructure changes
cd infrastructure/terraform && terraform apply
```

## Architecture

**Routing** — `react-router-dom` v6 with `createBrowserRouter`. All routes registered in `src/index.jsx`. Root path (`/`) is the landing page (`App.jsx`); inner pages under `/home`, `/projects`, `/resume`, `/contact`.

**Design system** — CSS custom properties in `src/index.css` (`:root`). Key tokens: `--font-display` (DM Serif Display), `--font-body` (Inter), `--accent` (#4F6EF7), `--bg` (#F8F9FE). Shared utility classes (`btn-primary`, `btn-secondary`, `section-label`, `page-wrapper`, `container`) live in `index.css` as globals.

**Page layout convention** — every inner page uses `<div className="page-wrapper">` with `<NavBar />` at top and `<Footer />` at bottom.

**Project data** — `src/components/projects.js` is the single source of truth for the portfolio. ESM exports (`export { projects, diff_text, date_string, same_date }`). Use named imports, not `require()`.

**Resume page** — `react-pdf` v9. Worker initialized via `new URL('pdfjs-dist/build/pdf.worker.min.mjs', import.meta.url)`. PDF served from `public/Resume_Tyler_Du.pdf`. `pdfjs-dist` excluded from Vite pre-bundler via `optimizeDeps.exclude`.

**Contact form** — POSTs to `${VITE_API_URL}/api/contact`. For local dev, set `VITE_API_URL=http://localhost:8000` in `.env.local`. CORS is configured in FastAPI middleware only (not API Gateway).

**Hosting** — Frontend: S3 bucket `whoistylerdu.com` (us-west-1) + CloudFront distribution `E23G2M0PQP2735`. Backend: Lambda `portfolio-api` (us-east-1) behind API Gateway at `api.whoistylerdu.com`.

## Infrastructure (AWS)

**Account**: 416469482962 | **Backend region**: us-east-1 | **Frontend S3 region**: us-west-1

**Terraform state**: `s3://rcos-terraform/portfolio/api/terraform.tfstate` + `terraform_tf_lockid` DynamoDB (both pre-existing)

**Do not import into Terraform**: CloudFront distribution `E23G2M0PQP2735` and existing ACM cert `1cda7e15-0ac8-4eee-87e2-2075ae84b41e` — managed manually, modifying them risks frontend downtime.

**Route53 zone**: `Z018519720Z0JNEXD5A5B` for `whoistylerdu.com`

**SES**: `tyleryeedu@gmail.com` verified as sending identity. Account starts in sandbox — request production access in AWS console (SES → Account dashboard) before the contact form can receive messages from unverified senders.

**Lambda auto-rebuild**: `null_resource.lambda_build` in `main.tf` re-runs `pip install` and repackages whenever any `.py` file or `requirements.txt` changes. Requires `pip` on PATH and builds a manylinux2014_x86_64 compatible package.

## Phase 3 (planned)

Agentic AI ("Ask Tyler") — Claude-powered agent with Tyler's resume/projects as grounding context. Recruiters paste a JD; agent evaluates fit and surfaces relevant work examples. Implementation: new router in the existing FastAPI backend + new page/component in the frontend. The `projects.js` data and `Resume_Tyler_Du.pdf` are the primary knowledge sources.
