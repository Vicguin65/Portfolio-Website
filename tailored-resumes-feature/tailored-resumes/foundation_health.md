<!-- company: Foundation Health -->

# Software Engineer, Early Career at Foundation Health

*Tailored from `foundation_health.md` | Match: **Good***

Tyler is a 2025 CS grad already shipping production code at a startup, works AI-native with Claude Code daily, and has clear learning-velocity evidence (production Rust within months of first using it, a deployed Discord bot built in 3 days). The gaps are stack-shaped: the job's Node/TypeScript backend work is not in his history (his backends are Python FastAPI and Django, with TypeScript used on a Tauri/React frontend), his GCP use is described only at the multi-cloud deployment level, and nothing in the sources documents test coverage, testing frameworks, or healthcare domain work. The JD explicitly discounts stack mismatch in favor of learning velocity, which is where he is strongest.

---

## Tyler Du

Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com  
linkedin.com/in/tyler-du-link | github.com/Vicguin65  

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Built the AWS account provisioning pipeline behind customer signup for the Actualize identity platform, automating a **25-minute** manual setup and supporting **50+ accounts daily**
- Shipped production **Rust** on the Actualize desktop client (**Tauri** shell, **React** and **TypeScript** frontend) months after first using the language, owning cross-platform binary packaging
- Use **Claude Code** daily as a core part of the workflow, reviewing agent-generated code before it ships

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Built an open-source **REST API** for the AWS Identity Store serving **100+ IBM teams** daily, integrated with IBM Security Verify for single sign-on
- Closed a gap in AWS's **SCIM API** by merging its responses with the Identity Store SDK, returning complete user records from one endpoint

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led **6 interns** shipping an educational bot with **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, deployed in **8 courses**
- Automated hiring workflows via the **Lever API**, saving **100+ hours** per season, and trained a **scikit-learn** resume classifier on 1,700+ records at **88% accuracy**


### PROJECTS

**Who is Tyler Du, Portfolio Site with AI Agent | React, FastAPI, AWS Lambda, Claude**
*Full-Stack Engineer | Sept 2024 - Present*

- Built the full stack solo: **React 18** and Vite frontend, Python **FastAPI** backend on **AWS Lambda**, infrastructure in **Terraform**
- Implemented an AI agent that uses **Claude** to evaluate candidate fit against a pasted job description

**Dandy's World Discord Bot | Python, discord.py, AWS EC2**
*Solo Developer | Oct 2024*

- Built and shipped a Discord bot in **3 days** that automates party and channel creation, running 24/7 on **EC2**


### SKILLS & AWARDS

**Languages:** TypeScript, JavaScript, Python, Rust, Java, C, C++, HCL

**Frameworks & Tools:** React, FastAPI, Django, PostgreSQL, Tauri, Git, Claude Code, Claude API, scikit-learn

**Cloud & Infrastructure:** GCP, AWS (Lambda, API Gateway, EC2, S3, IAM), Azure, Cloudflare, Terraform, Docker, CI/CD

**Awards & Certifications:** National Cyber Scholar with Honors, Dean's Honor List; AWS Cloud Practitioner, Terraform Associate


### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Data Structures, Algorithms, Software Design and Documentation, Distributed Systems

---

## Tailoring Notes

- Led with the Rust/Tauri bullet and the 3-day Discord bot to make learning velocity, which the JD names twice, the loudest signal.
- Moved TypeScript to the front of the languages line and GCP to the front of cloud, matching the Node/TypeScript/GCP stack named in the JD.
- Kept the Claude Code bullet but shortened it to the judgment point (reviewing agent output before it ships), which mirrors the JD's 'know when the output needs a second look'.
- Cut the multi-cloud Terraform and self-healing health checker bullets: strong infrastructure work, but this role is product feature delivery, not platform engineering.
- Cut the IBM Terraform VPC bullet and the AI Camp student grouping API bullet to hold one page after the previous draft overflowed.
- Trimmed the awards line and the coursework bullet to single lines rather than dropping the section, since 'sharp CS fundamentals' is an explicit requirement.

## Knowledge Base Gaps

The knowledge base has no evidence for the following. Answer these and add them to `knowledge_base.md` so future tailoring can draw on them.

### Node/TypeScript backend development (the stated production stack)  `blocking`

Have you built any server-side JavaScript or TypeScript (Node, Express, NestJS, Next.js API routes), and if so, what did the service do, who called it, and how much of it did you write versus inherit?

### Shipping features 'with proper test coverage'  `important`

Which testing frameworks have you actually written tests in (pytest, Jest/Vitest, Rust's test harness), and on which project did you own the test suite or CI test gate, including roughly what it covered and what it caught?

### GCP as the primary cloud  `important`

For the Actualize multi-cloud deployment, which specific GCP services did you configure or operate (GKE, Cloud Run, Cloud Functions, IAM, Pub/Sub, Cloud SQL), and what did you personally own on the GCP side?

### AI-native tooling beyond Claude Code (Cursor, 'the lot')  `nice-to-have`

Besides Claude Code, which AI coding tools have you used in a real workflow (Cursor, Copilot, Codex), and can you give a concrete example where the output was wrong and how you caught it?

### Product/domain curiosity in a regulated or clinical domain  `nice-to-have`

In the security and identity work at Zero Sum Defense, is there a case where you pushed back on or reshaped a requirement after learning how the end user actually worked, and what changed as a result?

### Frontend UX ownership and filing bugs/UX issues proactively  `nice-to-have`

On the Actualize desktop client or Accessible Routes, which user-facing screens or flows did you build end to end, and did you ever surface a UX problem yourself that led to a change being shipped?

