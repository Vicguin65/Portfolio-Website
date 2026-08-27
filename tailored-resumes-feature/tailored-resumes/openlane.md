<!-- company: OPENLANE -->

# Software Developer at OPENLANE

*Tailored from `openlane.md` | Match: **Good***

Tyler has strong backing for the cloud, CI/CD, serverless, REST API, and React parts of this role, with production AWS/GCP/Azure work and Terraform IaC at Zero Sum Defense. The gaps are notable though: no evidence of Kubernetes, PHP/Laravel, MySQL/MS SQL or NoSQL, or automated testing frameworks, and his containerization experience is limited to Docker deployments without documented depth. He is also at roughly 2 years of professional experience, at the low end of the 2 to 5+ year band.

---

## Tyler Du

Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com  
linkedin.com/in/tyler-du-link | github.com/Vicguin65  

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Engineered and deployed the Actualize platform across **AWS**, **GCP**, **Azure**, and **Cloudflare**, ensuring high availability and cross-provider compatibility
- Automated provisioning of **50+ AWS accounts daily**, enabling scalable and consistent infrastructure deployment
- Built a weekly self-healing health checker per tenant that reconciles configuration against a source-of-truth API, eliminating configuration drift in single-tenant infrastructure
- Automated **CI/CD** pipelines and **Terraform** infrastructure-as-code to streamline deployments and accelerate feature releases

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | Jan 2023 - Dec 2023*

- Developed **REST APIs** in **Python/Django** over a **PostgreSQL** database that improved student grouping efficiency for **300+ students**
- Led a team of **6 interns** to ship an educational LLM bot with **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, deployed across **8 courses** at 60+ students each

**IBM**
*Software Engineering Intern | Jan 2024 - May 2024*

- Built an open-source **REST API** on **AWS Lambda** and **CloudFormation** for AWS Identity Center, serving 100+ IBM teams worldwide daily
- Integrated AWS Identity Store with IBM Security Verify for single sign-on across identity providers, working directly with IBM's cloud team


### PROJECTS

**Who is Tyler Du Portfolio | React, FastAPI, AWS Lambda, Terraform**
*Full-Stack Engineer | Sept 2024 - Present*

- Built a full-stack site solo: **React 18 + Vite** frontend and **Python FastAPI** backend deployed serverless on **AWS Lambda** via Mangum with API Gateway, CloudFront, S3, and Route53
- Integrated an **Anthropic Claude** agent that evaluates candidate fit against job descriptions; all infrastructure managed as code in **Terraform**

**Accessible Routes | RPI | Python, Django, Docker, AWS EC2, React**
*Fullstack Engineer | Sept 2023 - Nov 2024*

- Developed a **RESTful API** in **Django** serving campus accessibility data (stairs, elevators, ramps) to a **React** frontend for mobility-impaired students
- Containerized and deployed frontend and backend with **Docker** on **AWS EC2**, configuring domain and SSL certificates


### SKILLS & AWARDS

**Languages:** Python, JavaScript, TypeScript, Java, C, C++, Rust, HCL, SQL

**Frameworks & Tools:** React, FastAPI, Django, Docker, Terraform, CI/CD, Git/GitHub, PostgreSQL, Linux

**Cloud:** AWS (Lambda, API Gateway, S3, EC2, IAM, CloudFront, CloudFormation), GCP, Azure, Cloudflare

**Certifications:** AWS Certified Cloud Practitioner, Terraform Associate, GIAC Foundational Cybersecurity Technologies

**Awards:** National Cyber Scholar with Honors, Microsoft Engagement Program Scholarship, Dean's Honor List


### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*B.S. Computer Science | GPA: 3.6 | May 2025*


---

## Tailoring Notes

- Led with work experience since the role weighs professional cloud, CI/CD, and API delivery most heavily.
- Promoted IBM from projects to work experience as a real internship, merging the duplicate project entry to save lines.
- Kept the portfolio project first among projects because it demonstrates React frontend plus serverless microservice backend, both named in the job description.
- Surfaced Docker containerization in the Accessible Routes bullet since the role asks for containerize, troubleshoot, and build images.
- Cut the Terraform Automation, Discord bot, webscrape, and hiring automation entries as less relevant to a web/microservices product team.
- Trimmed from the prior draft: removed the Zero Sum Defense Claude Code bullet, the AI Camp REST API detail split, one portfolio bullet, and condensed the skills block to fit one page.

## Knowledge Base Gaps

The knowledge base has no evidence for the following. Answer these and add them to `knowledge_base.md` so future tailoring can draw on them.

### Kubernetes and container orchestration (backend microservices orchestrated by Kubernetes on AWS)  `blocking`

Have you deployed or operated anything on Kubernetes (EKS, GKE, or self-managed), and if so what services were running on it, how many clusters or pods, and what were you responsible for (manifests, Helm, autoscaling, debugging)?

### PHP / Laravel  `important`

Have you written any PHP or Laravel code in a job, class, or side project, and if so what did the application do and how large was it?

### Automated testing (unit, integration, functional)  `important`

What testing frameworks have you used (pytest, Jest, Cypress, etc.), and on which project did you write tests? Roughly what coverage or how many tests did you add, and were they wired into CI?

### MySQL / MS SQL and NoSQL databases  `important`

Beyond PostgreSQL, which databases have you worked with (MySQL, MS SQL, DynamoDB, MongoDB, Redis), on what project, and what were you doing with them (schema design, query tuning, migrations)?

### Microservices architecture at scale  `important`

Have you designed or maintained a system split into multiple services? How many services, how did they communicate (REST, gRPC, queues), and what was the traffic volume?

### Agile/Scrum team process, code reviews, release management  `important`

Describe your team's process at Zero Sum Defense: sprint length, how work is estimated, how many PRs you review per week, and how releases are cut and versioned (Gitflow, trunk-based, tags)?

### Docker depth (creating and building images, troubleshooting)  `important`

For the Accessible Routes deployment or any other work, did you author the Dockerfiles and compose files yourself? What base images, multi-stage builds, or registry workflow did you use, and what container issues did you debug?

### Mobile delivery (iOS and Android products)  `nice-to-have`

Have you built or contributed to any mobile app (native or React Native), and what did it do?

### Modern frontend UX work at product scale  `nice-to-have`

What is the most complex React UI you have shipped? How many screens or components, what state management approach, and did you work from designer handoffs (Figma) or a design system?

