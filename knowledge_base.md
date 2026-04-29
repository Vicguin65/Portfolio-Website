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
- Engineered and deployed the Actualize platform across multi-cloud environments (AWS, GCP, Azure, Cloudflare), ensuring high availability and cross-provider compatibility
- Automated provisioning of 50+ AWS accounts daily, enabling scalable and consistent cloud infrastructure deployment
- Developed Terraform-based infrastructure-as-code solutions to standardize deployments across AWS, GCP, and Azure, reducing configuration drift
- Automated CI/CD pipelines to streamline deployment workflows and accelerate feature releases
Technologies used: AWS, GCP, Azure, Cloudflare, Terraform, CI/CD

### AI Camp — Software Engineer Intern (January 2023 – December 2023)
Palo Alto, CA
- Developed REST APIs for a PostgreSQL database that improved student grouping efficiency, impacting over 300 students
- Led a team of 6 interns to implement NVIDIA NeMo guardrails with GPT-3.5-turbo for an educational Python/Colang bot that taught HTML
- Bot was deployed in 8 courses, instructing 60+ students per course
Technologies used: Python, Django, PostgreSQL, OpenAI GPT-3.5-turbo, NVIDIA NeMo, BeautifulSoup4, Selenium

### IBM — Software Engineering Intern (January 2024 – May 2024)
- Built an open-source REST API for the AWS Identity Store in collaboration with IBM's cloud team
- [TODO: add more detail — what problem did it solve? who used it? any scale/impact metrics?]
Technologies used: Python, AWS Lambda, AWS CloudFormation

### [TODO: Organization/Company] — [TODO: Role] (May 2022 – August 2022)
- Automated hiring workflows using Lever's API, saving over 100 hours per hiring season
- Trained a scikit-learn resume classifier on 1,700+ candidate records, achieving 88% accuracy over its first six months in production
- Hosted model on AWS S3
Technologies used: Python, Scikit-Learn, AWS S3

---

## Projects

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
[TODO: any additional context — was this merged upstream? how many people use it?]
GitHub: https://github.com/Vicguin65/IBM-Identity-Center-API
Technologies: Python, AWS Lambda, AWS CloudFormation

### Terraform Automation For Data Science App (May 2024 – August 2024)

Collaborated with three other students to automate the provisioning of an AWS VPC containing 2 public subnets, 2 private subnets, and 4 t2.large Ubuntu servers hosting a data science application about polygraph test accuracy.
[TODO: was this for a class? a research project?]
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

### Hiring Management System Automation (May 2022 – August 2022)
Automated parts of a hiring management workflow using Lever's API, saving 100+ hours per hiring season. Trained a scikit-learn resume classifier on 1,700+ historical candidate records, achieving 88% accuracy over its first six months in production. Model was hosted on AWS S3.
Technologies: Python, Scikit-Learn, AWS S3

---

## Skills

### Languages

- **Python** — Most proficient language. Used professionally (IBM, hiring automation) and across 5+ personal projects. Comfortable with async, OOP, scripting, and ML workflows.
- **JavaScript / TypeScript** — Used in all frontend projects. Comfortable with modern ES6+, React hooks, async/await.
- **[TODO: any others? SQL, Java, C++, etc.?]**

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
- **OpenAI API** — Used GPT-3.5-turbo for structured data extraction and as the backbone of an educational bot at AI Camp.
- [TODO: any PyTorch, TensorFlow, Hugging Face experience?]

### Other

- **Git / GitHub** — Daily use; comfortable with branching, PRs, conflict resolution.
- **Linux** — Comfortable on command line; used for server management (EC2 instances at Zero Sum Defense and personal projects).
- [TODO: any Kubernetes experience?]

---

## Accomplishments & Metrics

- Automated provisioning of **50+ AWS accounts daily** at Zero Sum Defense
- Deployed production platform across **4 cloud providers** (AWS, GCP, Azure, Cloudflare)
- Saved **100+ hours per hiring season** via Lever API automation
- Trained a resume classifier with **88% accuracy** on 1,700+ records
- Educational bot deployed in **8 courses**, reaching **60+ students per course** at AI Camp
- Led a **team of 6 interns** to ship a production LLM feature at AI Camp
- Scraped and structured **68,000+ faculty records** with minimal manual intervention
- Improved student grouping for **300+ students** at AI Camp
- Built Dandy's World Discord Bot in **3 days**, deployed to production on EC2
- [TODO: any RPI academic accomplishments — Dean's List, awards, research?]
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

[TODO: anything else you want the agent to know that doesn't fit above]
Examples:

- Open to relocation: [yes/no/specific cities]
- Looking for: [full-time / internship / contract]
- Ideal role type: [frontend / backend / full-stack / infrastructure / ML]
- Industries of interest: [e.g. fintech, developer tools, healthcare tech]
