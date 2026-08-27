<!-- company: Nooks.ai -->

# New Grad Software Engineer (Full-Stack) at Nooks.ai

*Tailored from `nooks.md` | Match: **Good***

Tyler is a May 2025 CS grad with strong fundamentals coursework, production shipping experience, and full-stack work spanning React frontends, Python backends (FastAPI, Django), REST APIs, and AWS deployment, plus hands-on LLM work (Claude API, Claude Code, NeMo guardrails, GPT-3.5-turbo) that maps well to an AI-agent product. The gaps are Node.js, TypeScript-heavy production work, and real-time collaboration or enterprise-scale systems, which the sources do not evidence; his current role is more infrastructure/platform than customer-facing product engineering. He also has no documented experience talking directly with customers or working from San Francisco.

---

## Tyler Du

Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com  
linkedin.com/in/tyler-du-link | github.com/Vicguin65

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Engineered and deployed the Actualize platform across **AWS**, **GCP**, **Azure**, and **Cloudflare**, ensuring high availability and cross-provider compatibility
- Designed and implemented a self-healing health checker where each tenant runs a weekly heartbeat against a source-of-truth API and auto-corrects to the expected configuration
- Automated provisioning of **50+ AWS accounts daily** and standardized multi-cloud deployments with **Terraform**, reducing configuration drift
- Used **Claude Code** daily as a core part of the development and feature delivery workflow

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - May 2024*

- Built an open-source **REST API** on **AWS Lambda** and **CloudFormation** for AWS Identity Center, serving 100+ IBM teams worldwide daily
- Integrated AWS Identity Store with IBM Security Verify for single sign-on across identity providers, working directly with IBM's cloud team

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | Jan 2023 - Dec 2023*

- Developed **REST APIs** over a **PostgreSQL** database in **Django**, including a survey-similarity grouping algorithm that improved grouping for **300+ students**
- Led a team of **6 interns** to ship an educational LLM bot with **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, deployed across **8 courses** at 60+ students each


### PROJECTS

**Who is Tyler Du, Portfolio and AI Agent | React, FastAPI, AWS Lambda, Claude**
*Full-Stack Engineer | Sept 2024 - Present*

- Built the entire stack solo: a **React 18 + Vite** frontend and a Python **FastAPI** backend deployed on **AWS Lambda** via Mangum, with infrastructure managed in **Terraform**
- Implemented an AI agent that reads a resume and knowledge base from **S3** and uses **Claude Sonnet** to evaluate candidate fit, applying prompt engineering and context management


**Accessible Routes | Rensselaer Polytechnic Institute | React, Django, Docker, AWS EC2**
*Fullstack Engineer | Sept 2023 - Nov 2024*

- Developed a **RESTful API** in Python and **Django** serving campus accessibility data (stairs, elevators, ramps) to surface turn-by-turn routes for mobility-impaired students
- Deployed frontend and backend with **Docker** on **AWS EC2**, configuring domain name and SSL certificates

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Data Structures, Algorithms, Software Design and Documentation, Machine Learning From Data, Distributed Systems and Algorithms

### SKILLS & AWARDS

**Languages:** Python, JavaScript, TypeScript, Java, C, C++, Rust, HCL

**Frameworks & Tools:** React, FastAPI, Django, PostgreSQL, Docker, Git, Linux, Terraform, CI/CD, AWS

**AI:** Anthropic Claude API, Claude Code, OpenAI GPT-3.5-turbo, NVIDIA NeMo, scikit-learn

---

## Tailoring Notes

- Led with work experience and put the portfolio AI agent project first, since it is the closest match to building LLM-powered product features end to end.
- Reframed AI Camp using the Grouping API detail from the knowledge base so the bullet shows API design plus algorithm work rather than only infrastructure.
- Cut the IBM Identity Store API and Terraform Automation projects: both are infrastructure-focused and less relevant than full-stack product work for this role.
- Dropped the cloud certifications line and the ZSD CI/CD bullet to save space for full-stack and AI evidence.
- Merged skills into four lines and split out an AI line to mirror the job's emphasis on LLM-powered products.

## Knowledge Base Gaps

The knowledge base has no evidence for the following. Answer these and add them to `knowledge_base.md` so future tailoring can draw on them.

### Node.js backend experience `important`

Have you written any backend service in Node.js or TypeScript on the server (Express, Nest, serverless handlers), and if so what did it do and how was it deployed?

### Production TypeScript on the frontend `important`

Which of your React projects were written in TypeScript rather than plain JavaScript, and roughly how large was the codebase you owned?

### Real-time collaboration or streaming systems `important`

Have you built anything real-time (WebSockets, server-sent events, pub/sub, live multi-user state), and what was the concurrency or message volume it handled?

### Working directly with customers and turning feedback into features `important`

Describe a time you talked to an actual user or customer about a problem and shipped a change because of it: who were they, what did they ask for, and what did you build?

### Enterprise-scale workflows and platform performance/scalability work `important`

What is the largest traffic or data volume a system you built has handled (requests per day, records processed, concurrent users), and what specific change did you make to improve its latency or reliability?

### Code review and code quality practice on a team `nice-to-have`

On what team have you regularly reviewed other engineers' pull requests, how many people were in the review rotation, and what standards or testing did you enforce?

### Hybrid work from San Francisco three days a week `blocking`

Are you able to relocate to the San Francisco Bay Area for a hybrid role, and what timeline would you need?

### Voice AI or agent orchestration systems `nice-to-have`

Beyond single-call LLM prompts, have you built multi-step agent workflows, tool calling, or voice/speech pipelines, and what did the architecture look like?
