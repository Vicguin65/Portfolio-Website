<!-- company: Salesforce -->

# Software Engineer (New Graduate) at Salesforce

*Tailored from `salesforce.md` | Match: **Good***

Tyler hits the core bar for the new grad role: a CS degree from RPI with algorithms and distributed systems coursework, professional coding experience at two companies plus an IBM collaboration, and hands-on Python, JavaScript/TypeScript, and React work in production. He is unusually strong on the 'even better' criteria, using Claude Code daily as part of his development workflow and having shipped LLM features with NeMo guardrails and the Claude API. The clear gaps are the testing side of the job description (unit/functional tests, automation frameworks, code coverage metrics) and telemetry-driven operational excellence, neither of which the knowledge base documents, and his production depth is in cloud infrastructure rather than large-scale Java application development.

---

## Tyler Du

Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com  
linkedin.com/in/tyler-du-link | github.com/Vicguin65  

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Data Structures, Algorithms, Software Design and Documentation, Machine Learning From Data, Distributed Systems and Algorithms, Ethical Hacking


### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Use **Claude Code** daily as a core part of the development workflow, guiding and reviewing agent-generated code for platform engineering and feature delivery
- Engineered and deployed the Actualize platform across **AWS**, **GCP**, **Azure**, and **Cloudflare**, ensuring high availability and cross-provider compatibility
- Designed a scheduled health checker that has each tenant verify its configuration weekly against a source-of-truth API and self-correct, eliminating configuration drift
- Automated provisioning of **50+ AWS accounts daily** and built **CI/CD** pipelines that accelerated feature releases

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | Jan 2023 - Dec 2023*

- Led a team of **6 interns** to ship an educational bot using **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, written in **Python** and Colang, deployed in **8 courses** reaching **60+ students** each
- Developed **REST APIs** over a **PostgreSQL** database with a survey-similarity grouping algorithm, improving grouping efficiency for **300+ students**
- Automated collection of **68,000+ faculty records** using BeautifulSoup4, Selenium, and the OpenAI API for structured extraction


### PROJECTS

**Who is Tyler Du, Portfolio Site with AI Agent | React, FastAPI, AWS Lambda, Claude**
*Full-Stack Engineer | Sept 2024 - Present*

- Built the full stack solo: **React 18** + Vite frontend and a **Python FastAPI** backend on **AWS Lambda** via Mangum, with infrastructure managed in **Terraform**
- Implemented an AI agent that reads a resume and knowledge base from **S3** and uses **Claude Sonnet** to evaluate candidate fit, applying prompt engineering and context management

**REST API For AWS Identity Store | IBM | Python, AWS Lambda, CloudFormation**
*Project Manager | Jan 2024 - May 2024*

- Built an open-source **REST API** serving over **100 IBM teams** worldwide daily for the IBM Cloud team, managing security and identity permissions
- Integrated AWS Identity Store with IBM Security Verify for single sign-on across identity providers, working around AWS SCIM API limitations


### SKILLS & AWARDS

**Programming Languages:** Python, Java, C, C++, Rust, JavaScript, TypeScript, HCL

**AI & Developer Tools:** Claude Code, Anthropic Claude API, OpenAI API, NVIDIA NeMo, scikit-learn, Git/GitHub, Docker, Linux

**Frameworks & Cloud:** React, FastAPI, Django, PostgreSQL, AWS (Lambda, API Gateway, EC2, S3, IAM), GCP, Azure, Terraform, CI/CD

**Awards & Certifications:** National Cyber Scholar with Honors, Microsoft Engagement Program Scholarship, Dean's Honor List; AWS Certified Cloud Practitioner, Terraform Associate, GIAC Foundational Cybersecurity Technologies

---

## Tailoring Notes

- Kept EDUCATION first since this is a new graduate program where the CS degree and coursework are screened directly.
- Led the Zero Sum Defense entry with daily Claude Code usage and review of agent-generated code, which maps to the job's 'even better' LLM and agentic tooling criteria.
- Promoted the portfolio site project ahead of older work because it is the clearest evidence of full-stack product building plus LLM integration.
- Reframed AI Camp around team leadership, REST API design, and Python, the object-oriented and professional coding signals the role asks for.
- Cut Accessible Routes and the Terraform Automation project to stay on one page, since infrastructure provisioning is less central to this product engineering role than API and application work.
- Did not claim SQL, unit testing, or telemetry experience anywhere, as the sources do not support them.

## Knowledge Base Gaps

The knowledge base has no evidence for the following. Answer these and add them to `knowledge_base.md` so future tailoring can draw on them.

### Writing unit and functional tests, driving code coverage, and building test automation frameworks  `blocking`

On which project did you write the most tests, what framework did you use (pytest, Jest, JUnit, etc.), and what code coverage or automation metrics did the team track?

### Fluency in object-oriented programming and design at a professional level  `important`

Can you describe a system where you designed the class structure yourself, what the main abstractions were, and why you chose that design over alternatives?

### Java or C++ used in a professional or substantial academic setting  `important`

What is the largest thing you have built in Java or C++, roughly how many lines, and was it coursework, a project, or professional work?

### SQL proficiency  `important`

What kinds of SQL have you written directly (joins, aggregations, indexing, query tuning) versus going through an ORM like Django's, and on what size datasets?

### Using telemetry and metrics to drive operational excellence  `important`

What monitoring, logging, or alerting tooling have you set up or used at Zero Sum Defense (CloudWatch, Datadog, etc.), and what specific metric or dashboard changed how the team operated?

### Building highly scalable products serving millions of users  `nice-to-have`

What is the highest request volume or user count of anything you have worked on, and what did you do specifically to handle that load?

### Working closely with product managers, UX, and performance engineers  `nice-to-have`

On which project did you work with non-engineering stakeholders such as a product manager or designer, and how did you handle requirement changes or disagreements?

