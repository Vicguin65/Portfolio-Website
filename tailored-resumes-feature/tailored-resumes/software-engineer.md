<!-- company: Software Engineer -->

# Software Engineer, Application & Product

*Hand-authored, not produced by `tailor_resume.py`. Targets entry-level and early-career application/product software engineering roles (SWE I, 0-2 years) rather than one specific job description. Rebuild the PDF with `render_resume.py software-engineer.md`.*

---

## Tyler Du

Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com
linkedin.com/in/tyler-du-link | github.com/Vicguin65

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Data Structures, Algorithms, Software Design and Documentation, Distributed Systems

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Ship production **Rust** on a cross-platform **Tauri** desktop client with a **React** and **TypeScript** frontend, reaching production code in a language new to me within months
- Debugged a native library resolution failure that reproduced only on clean installs, then moved the check into a build pipeline so per-target mismatches surface at build time instead of on user machines
- Built the AWS account provisioning pipeline behind customer signup, automating a **25-minute** manual setup and supporting **50+ accounts daily**
- Use **Claude Code** daily for feature delivery, scoping and reviewing agent-generated code before it ships

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Built an open-source **REST API** for the AWS Identity Store on **AWS Lambda**, serving **100+ IBM teams** daily
- Closed a gap in AWS's **SCIM** API by merging its responses with the AWS Identity Store SDK, returning complete user records and enabling single sign-on via IBM Security Verify

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led a team of **6 interns** shipping an educational bot with **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, deployed in **8 courses** reaching **60+ students** each
- Developed **REST APIs** over a **PostgreSQL** database with a survey-similarity grouping algorithm, improving grouping efficiency for **300+ students**

### PROJECTS

**Who is Tyler Du, Portfolio Site with AI Agent | React, FastAPI, AWS Lambda, Claude**
*Full-Stack Engineer | Sept 2024 - Present*

- Built the full stack solo: **React 18** and Vite frontend, **Python FastAPI** backend on **AWS Lambda**, infrastructure in **Terraform**
- Implemented an AI agent that reads a resume and knowledge base from **S3** and uses **Claude** to evaluate candidate fit against a pasted job description

**Accessible Routes | Rensselaer Polytechnic Institute | Python, Django, PostgreSQL, Docker**
*Full-Stack Engineer | Sept 2023 - Nov 2024*

- Developed a RESTful API in **Python** and **Django** serving campus accessibility data (stairs, elevators, ramps), containerized with **Docker** and deployed on **AWS EC2**

### SKILLS & AWARDS

**Languages:** Python, Rust, JavaScript, TypeScript, Java, C, C++, HCL

**Frameworks & Databases:** React, FastAPI, Django, PostgreSQL, Tauri, scikit-learn, NVIDIA NeMo, Claude API

**Tools & Practices:** Git, Docker, CI/CD, Linux, AWS (Lambda, API Gateway, EC2, S3, IAM), Terraform, Claude Code, object-oriented design, REST API design, code review

**Awards & Certifications:** National Cyber Scholar with Honors, Microsoft Engagement Program Scholarship, Dean's Honor List; AWS Certified Cloud Practitioner, HashiCorp Terraform Associate

---

## Tailoring Notes

- Reordered Zero Sum Defense to lead with application development (Rust and Tauri client, debugging, payment feature) and pushed infrastructure to a single bullet. The base resume leads with provisioning and drift remediation, which reads as platform engineering to a product SWE screener.
- Added the debugging story from the knowledge base. It carries the "debugging" keyword honestly and is a better engineering-judgment signal than another automation bullet.
- Restored the AI Camp REST API and grouping-algorithm bullet, cut from the base resume for space. It is the clearest application backend signal in the work history.
- Restored Accessible Routes for its Django, PostgreSQL, and REST API work.
- Cut the IBM Terraform and VPC bullet, the least relevant to product engineering.
- Cut for one-page fit: the payment-feature bullet, AI Camp's scikit-learn and Lever bullet, and one Accessible Routes bullet. The scikit-learn bullet (88% accuracy, 100+ hours saved) is the strongest candidate to swap back in if you drop something else.
- Added "object-oriented design", "REST API design", and "code review" to the skills block. All three are supported by the knowledge base; none are invented.
- Retitled the current role "Member of Technical Staff, Software Engineer" so it matches title searches. **Confirm this is accurate to your role before sending.**

## Knowledge Base Gaps

These are the keywords most common in entry-level SWE postings that the knowledge base cannot support. Answering them in `knowledge_base.md` would let every future tailoring run use them.

- **Testing.** The single biggest gap. Nearly every entry-level SWE posting asks for unit tests, test automation, or code coverage, and there is no testing evidence anywhere. The Actualize repo has pre-commit hooks and CI validate jobs, so there is likely a real answer here.
- **Agile / Scrum.** No evidence of sprint work, standups, or ticket workflow.
- **SQL.** PostgreSQL appears throughout, but whether you write raw SQL or only use the Django ORM is still unrecorded.
- **Java, C, C++.** Listed as languages with no supporting bullet anywhere. A screener will ask.
- **Microservices and system design.** No evidence recorded.
