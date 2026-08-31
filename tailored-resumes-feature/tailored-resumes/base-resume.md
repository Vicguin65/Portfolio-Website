<!-- company: Base -->

# Tyler Du, Standing Resume

The base resume, and the source of truth for `Resume_Tyler_Du.pdf`. Edit the body below, then rebuild the PDF:

    python tailored-resumes-feature/scripts/render_resume.py base-resume.md -o Resume_Tyler_Du.pdf
    aws s3 cp Resume_Tyler_Du.pdf s3://whoistylerdu.com/Resume_Tyler_Du.pdf --cache-control "max-age=86400" --region us-west-1

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

- Built the AWS account provisioning pipeline behind customer signup for the **Actualize** identity platform, automating a **25-minute** manual setup and supporting **50+ accounts daily**
- Designed a self-healing health checker running weekly on **EventBridge**, comparing each tenant's configuration against expected state and correcting drift automatically
- Deployed Actualize across **AWS**, **GCP**, **Azure**, and **Cloudflare**, standardizing multi-cloud infrastructure with **Terraform** modules and automated **CI/CD**
- Shipped production **Rust** on the **Tauri** desktop client months after first using the language, owning cross-platform binary packaging and a build pipeline that catches per-target mismatches
- Use **Claude Code** daily for infrastructure automation and feature delivery, reviewing agent-generated code before it ships

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Built an open-source **REST API** for the AWS Identity Store serving **100+ IBM teams** daily, integrated with IBM Security Verify for single sign-on across identity providers
- Closed a gap in AWS's **SCIM** API by merging its responses with the AWS Identity Store SDK, returning complete user records from one endpoint
- Automated provisioning of an AWS **VPC** and 4 EC2 servers hosting a data science application with **HCP Terraform**, including deployment of application updates

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led a team of **6 interns** shipping an educational bot with **NVIDIA NeMo** guardrails and **GPT-3.5-turbo**, deployed in **8 courses** reaching **60+ students** each
- Automated hiring workflows via the Lever API, saving **100+ hours per season**, and trained a **scikit-learn** resume classifier on 1,700+ records at **88% accuracy**

### PROJECTS

**Who is Tyler Du, Portfolio Site with AI Agent | React, FastAPI, AWS Lambda, Claude**
*Full-Stack Engineer | Sept 2024 - Present*

- Built the full stack solo: **React 18** and Vite frontend, **Python FastAPI** backend on **AWS Lambda**, infrastructure in **Terraform**
- Implemented an AI agent that reads a resume and knowledge base from **S3** and uses **Claude** to evaluate candidate fit against a pasted job description

### SKILLS & AWARDS

**Languages:** Python, Rust, JavaScript, TypeScript, Java, C, C++, HCL

**Cloud & Infrastructure:** AWS (Lambda, API Gateway, EC2, S3, IAM), GCP, Azure, Cloudflare, Terraform, Docker, CI/CD

**Frameworks & Tools:** React, FastAPI, Django, PostgreSQL, Tauri, Git, Claude Code, Claude API, scikit-learn

**Awards & Certifications:** National Cyber Scholar with Honors, Microsoft Engagement Program Scholarship, Dean's Honor List; AWS Certified Cloud Practitioner, HashiCorp Terraform Associate, GIAC Foundational Cybersecurity Technologies
