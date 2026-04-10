# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

```
portfolio-website/          React frontend (Vite)
  index.html                Vite entry HTML (root level — not public/)
  vite.config.js            Vite config; allows JSX in .js files; excludes pdfjs-dist from pre-bundler
  src/
    index.js                Router setup — all routes defined here
    index.css               Design tokens (CSS custom properties) + global reset + shared utilities
    App.js / App.css        Landing page (full-viewport hero, floating CSS blob animations)
    components/
      NavBar.js/.css        Sticky navbar; blur-on-scroll; mobile hamburger; active-link state
      Footer.js/.css        LinkedIn, GitHub, Email links
      projects.js           Project data array + date utilities — ESM exports
    pages/
      HomePage.js/.css      About + skills grid
      ProjectPage.js/.css   Auto-sorted project card grid
      ResumePage.js + .module.css   PDF viewer (react-pdf) with zoom toggle
      ContactPage.js + .module.css  Contact form (Phase 2: POST to FastAPI)
      NotFoundPage.js/.css

backend/                    Python FastAPI backend (Phase 2 — not yet created)
```

## Commands

All commands run from `portfolio-website/`:

```bash
npm run dev      # Dev server (localhost:5173)
npm run build    # Production build → dist/
npm run preview  # Preview production build locally
```

Install after pulling:
```bash
npm install
```

## Architecture

**Routing** — `react-router-dom` v6 with `createBrowserRouter`. All routes registered in `src/index.js`. Root path (`/`) is the landing page (`App.js`); inner pages under `/home`, `/projects`, `/resume`, `/contact`.

**Design system** — CSS custom properties defined in `src/index.css` (`:root`). All components use `var(--token-name)`. Key tokens: `--font-display` (DM Serif Display), `--font-body` (Inter), `--accent` (#4F6EF7), `--bg` (#F8F9FE). Shared utility classes (`btn-primary`, `btn-secondary`, `section-label`, `page-wrapper`, `container`) also live in `index.css`.

**Page layout convention** — every inner page uses `<div className="page-wrapper">` (flex column, min-height 100vh) with `<NavBar />` at top and `<Footer />` at bottom. `<main>` gets `flex: 1` automatically.

**Project data** — `src/components/projects.js` is the single source of truth. Uses ESM exports (`export { projects, diff_text, date_string, same_date }`). Import with named imports (not `require`).

**Vite + JSX in .js files** — configured via `react({ include: ['**/*.{js,jsx}'] })` in `vite.config.js`. Files intentionally kept as `.js` to avoid mass rename churn.

**Resume page** — `react-pdf` v9 with `pdfjs-dist`. Worker initialized via `new URL('pdfjs-dist/build/pdf.worker.min.mjs', import.meta.url)`. PDF file served from `public/Resume_Tyler_Du.pdf`. `pdfjs-dist` is excluded from Vite's pre-bundler (`optimizeDeps.exclude`).

**Hosting** — AWS (target). Frontend will be served via S3/CloudFront or similar. Backend (Phase 2) will be FastAPI on AWS Lambda or EC2.

## Planned Phases

- **Phase 2**: Python FastAPI backend — contact form endpoint, infrastructure for AI features. Deploy on AWS.
- **Phase 3**: Agentic AI ("Ask Tyler") — Claude-powered agent with Tyler's resume/project context; recruiters can drop JDs and get fit analysis.
