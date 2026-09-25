<!-- company: Software Engineer -->

# Software Engineer, Application & Product

*Hand-authored, not produced by `tailor_resume.py`. Targets entry-level and early-career application/product software engineering roles (SWE I, 0-2 years) rather than one specific job description. Rebuild the PDF with `render_resume.py software-engineer.md`.*

---

## Tyler Du

Reno, NV | (775) 997-8654 | tyleryeedu@gmail.com | whoistylerdu.com
linkedin.com/in/tyler-du-link | github.com/Vicguin65

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Data Structures, Algorithms, Software Design and Documentation, Distributed Systems

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN (Remote)
*Member of Technical Staff | July 2025 - Present*

- Ship production **Rust** on the **Tauri** desktop client (**React** and **TypeScript** frontend) within months of first using the language
- Built the browser-automation flow behind the client's in-app payment feature, handling multi-step checkout and verification
- Debugged a hardware-token login failure that reproduced only on clean installs, traced it to per-target native binaries, and wrote the build scripts **GitLab CI** runs for Windows, macOS, and Linux so a bad binary surfaces in CI
- Built the AWS account provisioning pipeline behind customer signup, replacing a **25-minute** manual setup with a zero-touch flow that has provisioned nearly **20,000 accounts**, tracked in **DynamoDB**
- Use **Claude Code** daily for feature delivery, scoping and reviewing agent-generated code before it ships

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Built an open-source **REST API** for the AWS Identity Store on **AWS Lambda**, serving **100+ IBM teams** daily
- Closed a gap in AWS's **SCIM** API by merging its responses with the AWS Identity Store SDK, returning complete user records and enabling single sign-on via IBM Security Verify

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led a team of **6 interns** shipping an educational bot with **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, deployed in **8 courses** reaching **60+ students** each
- Built **Django REST APIs** on **PostgreSQL**, including cohort grouping for **300+ students**, and trained a **scikit-learn** resume classifier that held **88% accuracy** over six months in production

### PROJECTS

**Who is Tyler Du, Portfolio Site with AI Agent** | github.com/Vicguin65/Portfolio-Website
*Personal project | Sept 2024 - Present*

- Built the full stack solo: **React 18** and Vite frontend, **Python FastAPI** backend on **AWS Lambda**, infrastructure in **Terraform**
- Implemented an AI agent that reads a resume and knowledge base from **S3** and uses **Claude** to evaluate candidate fit against a pasted job description

**Accessible Routes | Rensselaer Polytechnic Institute** | github.com/Accessible-Routes
*Full-Stack Engineer | Sept 2023 - Nov 2024*

- Built the backend REST API from scratch in **Python** and **Django**, serving campus accessibility data (stairs, elevators, ramps) that powers turn-by-turn accessible routes, deployed on **AWS EC2**

### SKILLS & AWARDS

**Languages:** Python, Rust, TypeScript, JavaScript, HCL

**Frameworks & Databases:** React, FastAPI, Django, Tauri, PostgreSQL, DynamoDB, scikit-learn, NVIDIA NeMo, Claude API

**Tools & Practices:** Git, GitLab CI/CD, Docker, Linux, AWS (Lambda, API Gateway, EC2, S3, IAM), Terraform, Claude Code, object-oriented design, REST API design, code review

**Certifications & Awards:** AWS Certified Cloud Practitioner, HashiCorp Terraform Associate; National Cyber Scholar with Honors, Microsoft Engagement Program Scholarship, Dean's Honor List

---

## Tailoring Notes

*Refreshed 2026-09-25 against the knowledge base as of 2026-09-21 and the current base resume.*

- Zero Sum Defense still leads with application work, now with the payment-flow bullet restored in second place (the base resume carries it too). It is the clearest product-feature bullet in the current role.
- Rewrote the debugging bullet. The old one said the fix was moved "into a build pipeline", which reads as owning the pipeline; the knowledge base says the Tauri CI pipeline was a teammate's. It now claims only the per-target build scripts GitLab CI runs.
- Removed first person ("a language new to me") from the Rust bullet and cut it to one line.
- Dropped the tech stack from both project headers in favor of their GitHub links, matching the base resume; the stack still appears in the bullets and skills.
- Updated the provisioning bullet to nearly 20,000 accounts (19,889 as of 2026-09-15) and tied DynamoDB to it, since the knowledge base now calls DynamoDB Tyler's strongest database.
- Folded the AI Camp grouping work into a phrase inside a combined REST API and scikit-learn bullet. The knowledge base asks that it stay a phrase, not a bullet of its own, and the old "survey-similarity grouping algorithm, improving grouping efficiency" wording no longer matches the recorded detail.
- Removed "containerized with Docker" from Accessible Routes. Docker has never had any backing in the knowledge base, and the project's recorded stack is React, Django, and EC2. The bullet now uses the "built the backend API from scratch" detail instead.
- Dropped Java, C, and C++ from languages, matching the base resume, since nothing backs them yet.
- Removed the old note about retitling the role "Member of Technical Staff, Software Engineer". The resume uses the real title.
- Candidate swap-in if a posting values mentoring or communication: the RPI Undergraduate Mentor role (Foundations of CS, Intro to Algorithms, RCOS; Aug 2023 to Aug 2024), now in the knowledge base. Accessible Routes is the natural thing to cut for it.

## Knowledge Base Gaps

These are the keywords most common in entry-level SWE postings that the knowledge base cannot support. Answering them in `knowledge_base.md` would let every future tailoring run use them.

- **Testing.** Now recorded as a firm no: there are no authored test suites as of September 2026, so do not claim it. This is still the biggest gap for SWE screens. Writing even a small test suite (for example, for this portfolio's FastAPI backend) would close it honestly.
- **Agile / Scrum.** No evidence of sprint work, standups, or ticket workflow.
- **SQL.** PostgreSQL appears throughout, but whether you write raw SQL or only use the Django ORM is still unrecorded.
- **Java, C, C++.** Dropped from this resume for lack of backing. If any were used beyond coursework, record it and they can come back.
- **Docker.** Still listed in skills with no context behind it. If it can't be backed, drop it here too.
- **Microservices and system design.** No evidence recorded.
