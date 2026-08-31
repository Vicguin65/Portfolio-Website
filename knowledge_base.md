# Tyler Du — Professional Knowledge Base

This is the agent's primary grounding context. Fill in the TODO sections with your own details.
Upload to S3 after any update: `aws s3 cp knowledge_base.md s3://whoistylerdu.com/knowledge_base.md --region us-west-1`

---

## Education

**Rensselaer Polytechnic Institute (RPI)** — Troy, NY
B.S. Computer Science | May 2025
GPA: 3.61/4.0
Relevant coursework: Data Structures, Algorithms, Software Design and Documentation, Machine Learning From Data, Distributed Systems and Algorithms, Ethical Hacking

---

## Work Experience

### Zero Sum Defense — Member of Technical Staff (July 2025 – Present)

Minneapolis, MN

Actualize is Zero Sum Defense’s identity platform.

- Engineered and deployed the Actualize platform across multi-cloud environments (AWS, GCP, Azure, Cloudflare), ensuring high availability and cross-provider compatibility
- Built the automated AWS account provisioning pipeline that runs whenever a customer signs up, replacing a manual setup that took roughly 25 minutes per account; it now supports 50+ account creations daily
- Developed Terraform-based infrastructure-as-code solutions to standardize deployments across AWS, GCP, and Azure, reducing configuration drift
- Automated CI/CD pipelines to streamline deployment workflows and accelerate feature releases
- Designed and implemented a health checker that solves configuration drift in single-tenant infrastructure. Triggered weekly on an EventBridge schedule, it compares each tenant’s configuration against the expected state and self-corrects any drift, keeping every tenant in sync without giving up the blast-radius isolation that single-tenancy provides
- Contributed to the Actualize desktop client, a Tauri application with a React and TypeScript frontend and a Rust backend, including packaging the native binaries its hardware-token authentication depends on so the flow works on a clean install
- Built a browser-automation flow for the client’s in-app payment feature, handling multi-step checkout and additional verification steps
- Use Claude Code daily as a core part of the development workflow, applying agentic AI coding to infrastructure automation, platform engineering, and feature delivery
  Technologies used: AWS, GCP, Azure, Cloudflare, Terraform, CI/CD, Python, Rust, Tauri, React, TypeScript, Claude Code

### IBM — Software Engineering Intern (January 2024 – August 2024)

Troy, NY

Two projects across two terms: the AWS Identity Store REST API (January – May 2024), then Terraform automation for a data science application (May – August 2024).

- Built an open-source REST API for the AWS Identity Store in collaboration with IBM’s cloud team, serving 100+ IBM teams worldwide daily for security and identity permission management
- Integrated AWS Identity Store with IBM Security Verify to enable single sign-on across identity providers
- Solved a data completeness gap in AWS’s SCIM API, which omits several User fields: the API merges the SCIM response with data pulled from the AWS Identity Store Python SDK, which does expose those fields, so callers get a complete user record from a single endpoint
- Built a Terraform automation tool for the IBM Cloud team that provisions an AWS VPC with 2 public and 2 private subnets and 4 t2.large Ubuntu servers hosting a data science React application, and automated deployment of application updates onto it
  Technologies used: Python, AWS Lambda, AWS CloudFormation, AWS Identity Store SDK, SCIM, HCP Terraform, AWS VPC, React

### AI Camp — Software Engineer Intern (May 2022 – December 2023)

Palo Alto, CA

Interned across multiple semesters (not continuous, split around school terms), starting on internal hiring tooling before moving to student-facing platform and LLM work.

- Automated hiring workflows using Lever’s API, saving over 100 hours per hiring season; the tooling ran across two full hiring cycles
- Trained a scikit-learn resume classifier on 1,700+ candidate records, achieving 88% accuracy over its first six months in production; model hosted on AWS S3
- Developed REST APIs for a PostgreSQL database that improved student grouping efficiency, impacting over 300 students
- Led a team of 6 interns to implement NVIDIA NeMo guardrails with GPT-3.5-turbo for an educational Python/Colang bot that taught HTML
- Bot was deployed in 8 courses, instructing 60+ students per course
  Technologies used: Python, Django, PostgreSQL, Scikit-Learn, Lever API, OpenAI GPT-3.5-turbo, NVIDIA NeMo, BeautifulSoup4, Selenium, AWS S3

---

## Projects

### Actualize Desktop Client (November 2025 – present) — Zero Sum Defense

Cross-platform desktop application for the Actualize platform, built with Tauri: React and TypeScript in the frontend, Rust for the native backend.
Contributed across the client and owned packaging of the native binaries behind its hardware-token authentication, resolving the library-loading failures that broke the flow on machines without a developer toolchain installed.
Also built a browser-automation flow for the in-app payment feature, covering multi-step checkout and additional verification steps.
Technologies: Rust, Tauri, React, TypeScript, AWS SDK for Rust

### "Who is Tyler Du" — Personal Portfolio Website (September 2024 – present)

Full-stack personal portfolio with an AI agent ("Ask Tyler") that evaluates candidate fit for job descriptions using Claude.
Built the entire stack solo: React 18 + Vite frontend, Python FastAPI backend deployed on AWS Lambda via Mangum, infrastructure managed with Terraform.
The AI agent fetches the resume from S3, reads this knowledge base, and uses Claude Sonnet to evaluate fit.
GitHub: https://github.com/Vicguin65/Portfolio-Website
Technologies: React, FastAPI, AWS Lambda, API Gateway, CloudFront, S3, SES, Route53, Terraform, Anthropic Claude

### Accessible Routes — Campus Accessibility Routing (September 2023 – November 2024)

Web application that provides accessible routes between buildings on RPI's campus using RPI's accessibility infrastructure data.
Built the backend API from scratch; the frontend surfaces turn-by-turn accessible routes for mobility-impaired students.
[TODO: any usage metrics? how many users? was it deployed publicly?]
GitHub: https://github.com/Accessible-Routes
Technologies: React, Django, CSS, AWS EC2

### REST API For AWS Identity Store (January 2024 – May 2024)

Open-source project in collaboration with IBM's cloud team. Built a REST API layer on top of AWS Identity Center (formerly SSO) to simplify identity management operations.
Serves 100+ IBM teams worldwide on a daily basis. Works around a gap in AWS’s SCIM API, which omits several User fields, by merging the SCIM response with data from the AWS Identity Store Python SDK so callers get a complete user record from one endpoint.
[TODO: was this merged upstream, and is it still in use?]
GitHub: https://github.com/Vicguin65/IBM-Identity-Center-API
Technologies: Python, AWS Lambda, AWS CloudFormation

### Terraform Automation For Data Science App (May 2024 – August 2024) — IBM

Collaborated with three other students to automate the provisioning of an AWS VPC containing 2 public subnets, 2 private subnets, and 4 t2.large Ubuntu servers hosting a data science application about polygraph test accuracy.
Built during the second term of the IBM internship (May – August 2024) for the IBM Cloud team.
GitHub: https://github.com/Vicguin65/IBM-Terraform-Automation
Technologies: HCP Terraform CDK, AWS VPC, React

### Dandy's World Discord Bot (October 2024 — built in 3 days)

Discord bot built in 3 days, inspired by a Roblox game. Automates the creation of parties, text channels, and voice channels via slash commands. Runs 24/7 on an AWS EC2 t3.micro Ubuntu server.
GitHub: https://github.com/Vicguin65/Dandy-World-Discord-Bot
Technologies: Python, discord.py, AWS EC2

### NeMo Guardrails Educational Bot (June 2023 – December 2023) — AI Camp

Led a team of 6 interns to build an educational chatbot using NVIDIA NeMo guardrails and GPT-3.5-turbo. The bot was written in Python and Colang and taught HTML to students. Deployed across 8 courses reaching 60+ students per course.
Technologies: Python, Colang, NVIDIA NeMo, OpenAI GPT-3.5-turbo

### School Contacts Webscrape (June 2023) — AI Camp

Built for AI Camp. Automated collection of school contact information via web scraping, gathering 68,000+ faculty member records. Used BeautifulSoup4 for static pages, Selenium for dynamic pages, and the OpenAI GPT-3.5-turbo API for structured data extraction from unstructured text.
Technologies: Python, BeautifulSoup4, Selenium, OpenAI GPT-3.5-turbo

### Grouping API for Camp Students (January 2023 – April 2023) — AI Camp

Built for AI Camp. Django REST API to model and manage groups of students. Implemented a grouping algorithm that matches students by survey similarity score. Processed data for ~300 students; directly improved student grouping efficiency across AI Camp programs.
Technologies: Python, Django, PostgreSQL

### Hiring Management System Automation (May 2022 – August 2022) — AI Camp

Built for AI Camp. Ran across two full hiring cycles. Automated parts of a hiring management workflow using Lever's API, saving 100+ hours per hiring season. Trained a scikit-learn resume classifier on 1,700+ historical candidate records, achieving 88% accuracy over its first six months in production. Model was hosted on AWS S3.
Technologies: Python, Scikit-Learn, AWS S3

---

## Skills

### Languages

- **Python** — Most proficient language. Used professionally (IBM, hiring automation) and across 5+ personal projects. Comfortable with async, OOP, scripting, and ML workflows.
- **JavaScript / TypeScript** — Used in all frontend projects. Comfortable with modern ES6+, React hooks, async/await.
- **Rust** — Production use at Zero Sum Defense on the Actualize desktop client, whose native backend is written entirely in Rust behind a Tauri shell. Worked across the client and owned its native binary packaging and build configuration.
- **HCL / Terraform** — Primary language for infrastructure work at Zero Sum Defense and across personal projects.
- **Java, C, C++** — [TODO: coursework only, or used on a real project? Add context so tailored resumes can back these up.]
- **SQL** — [TODO: what level? Used through the Django ORM only, or hand-written queries too?]

### Frontend

- **React** (3+ years) — Built multiple production applications. Comfortable with hooks, React Router, state management, and Vite tooling.
- [TODO: any design systems, testing frameworks, etc.?]

### Backend

- **FastAPI** — Used for portfolio backend; familiar with async routes, Pydantic validation, Mangum Lambda adapter.
- **Django** — Used in Accessible Routes and Grouping API; comfortable with ORM, REST framework, views.
- [TODO: any experience with Express, Flask, Spring, etc.?]

### Cloud & Infrastructure

- **AWS** — Most-used cloud platform. Production experience at Zero Sum Defense and IBM. Hands-on with: Lambda, API Gateway, S3, CloudFront, SES, EC2, IAM, Route53, ACM, CloudFormation. Automated provisioning of 50+ accounts daily at ZSD.
- **GCP** — Used in production at Zero Sum Defense for multi-cloud deployments.
- **Azure** — Used in production at Zero Sum Defense for multi-cloud deployments.
- **Cloudflare** — Used at Zero Sum Defense for the Actualize platform.
- **Terraform** — Production use at Zero Sum Defense (multi-cloud IaC across AWS/GCP/Azure) and personal projects; familiar with modules, state management, providers.
- **CI/CD** — Automated deployment pipelines at Zero Sum Defense.
- **Docker** — [TODO: add context — used for local dev? CI/CD? deployments?]

### Databases

- **PostgreSQL** — Used in Grouping API and Accessible Routes.
- [TODO: any MySQL, MongoDB, Redis, DynamoDB experience?]

### AI / ML

- **scikit-learn** — Built and deployed a resume classifier with 88% accuracy trained on 1,700+ records.
- **NVIDIA NeMo** — Used at AI Camp to implement guardrails for an educational LLM bot in production (8 courses, 60+ students each).
- **Anthropic Claude API** — Integrated into portfolio agent; familiar with prompt engineering, system prompts, context management.
- **Claude Code (agentic coding)** — Daily driver at Zero Sum Defense across infrastructure automation, platform engineering, and feature work, alongside personal projects such as this portfolio site and its resume-tailoring CLI. Used it to ship production Rust on the Actualize desktop client: scoping each change, directing the agent through the Tauri and native-binary toolchain, and reviewing generated code before it shipped rather than accepting output wholesale. Also used it to build the client’s browser-automation payment flow, iterating against a real multi-step checkout until the flow handled its verification steps reliably.
- **OpenAI API** — Used GPT-3.5-turbo for structured data extraction and as the backbone of an educational bot at AI Camp.
- [TODO: any PyTorch, TensorFlow, Hugging Face experience?]

### Other

- **Git / GitHub** — Daily use; comfortable with branching, PRs, conflict resolution.
- **Linux** — Comfortable on command line; used for server management (EC2 instances at Zero Sum Defense and personal projects).
- [TODO: any Kubernetes experience?]

---

## Certifications & Awards

### Certifications

- **AWS Certified Cloud Practitioner**
- **HashiCorp Terraform Associate**
- **GIAC Foundational Cybersecurity Technologies (GFACT)**
- **Associate Google Workspace Administrator**

### Awards

- **National Cyber Scholar with Honors** — 2021. One of 10 Nevada students named in that cohort; covered by the Nevada Department of Education.
- **Microsoft Engagement Program Scholarship**
- **Dean’s Honor List** — Rensselaer Polytechnic Institute
- **FBLA Gold, Computer Game and Simulation Programming** — high school. Kept here for grounding; generally should not appear on engineering resumes.

---

## Accomplishments & Metrics

- Automated provisioning of **50+ AWS accounts daily** at Zero Sum Defense, replacing a manual setup that took roughly **25 minutes per account**
- Deployed production platform across **4 cloud providers** (AWS, GCP, Azure, Cloudflare)
- Solved configuration drift in single-tenant infrastructure at Zero Sum Defense with a **weekly self-healing health checker** that detects and corrects drift on a schedule
- Saved **100+ hours per hiring season** via Lever API automation
- Trained a resume classifier with **88% accuracy** on 1,700+ records
- Educational bot deployed in **8 courses**, reaching **60+ students per course** at AI Camp
- Led a **team of 6 interns** to ship a production LLM feature at AI Camp
- Scraped and structured **68,000+ faculty records** with minimal manual intervention
- Improved student grouping for **300+ students** at AI Camp
- Built Dandy's World Discord Bot in **3 days**, deployed to production on EC2
- [TODO: any open-source contribution metrics — stars, forks, downloads?]
- [TODO: any user/traffic metrics for Accessible Routes?]

---

## Soft Skills & Working Style

[TODO: fill this in — it helps the agent give better interview talking points]
Examples:

- Comfortable working independently or in small teams
- Experience collaborating with cross-functional teams (IBM cloud team)
- Fast learner — built functional Discord bot in 3 days
- [TODO: how do you approach debugging? documentation? code review?]

---

## Other Context for the Agent

- Open to relocation: yes
- Looking for: full-time
- Ideal role type: [frontend / backend / full-stack / infrastructure / ML]
- Industries of interest: [e.g. fintech, developer tools, healthcare tech]
