<!-- company: Base -->

# Tyler Du, Standing Resume

The base resume, and the source of truth for `Resume_Tyler_Du.pdf`. Edit the body below, then rebuild the PDF:

    python tailored-resumes-feature/scripts/render_resume.py base-resume.md -o Resume_Tyler_Du.pdf
    aws s3 cp Resume_Tyler_Du.pdf s3://whoistylerdu.com/Resume_Tyler_Du.pdf --cache-control "max-age=86400" --region us-west-1

---

## Tyler Du

Reno, NV | (775) 997-8654 | tyleryeedu@gmail.com | whoistylerdu.com
linkedin.com/in/tyler-du-link | github.com/Vicguin65

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN (Remote)
*Member of Technical Staff | July 2025 - Present*

- Built the AWS account provisioning pipeline behind customer signup for the Actualize identity platform, replacing a 25-minute manual setup per account with a zero-touch flow that has provisioned **nearly 20,000 accounts** at 50+ a day
- Designed a self-healing drift checker, a weekly EventBridge job that reconciles each tenant against its expected state; it caught **200+ misconfigured tenants** on its first run while preserving single-tenancy's blast-radius isolation
- Built the browser-automation flow behind the desktop client's **in-app payment feature**, driving a multi-step checkout and its additional verification steps end to end
- Owned native binary packaging for hardware-token authentication in the Rust and Tauri desktop client, writing the per-target build scripts GitLab CI runs for Windows, macOS, and Linux so a bad binary **surfaces in CI, not on user machines**
- Built the autoscaling fleet of ephemeral **Windows EC2 GitLab runners** (Terraform) that the client's Windows builds run on
- Deployed Actualize across AWS, GCP, Azure, and Cloudflare with shared **Terraform** modules

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Built an open-source REST API for the AWS Identity Store (github.com/Vicguin65/IBM-Identity-Center-API) serving **100+ IBM teams** daily, integrated with IBM Security Verify for single sign-on across identity providers
- Closed a gap in AWS's SCIM API by merging its responses with the AWS Identity Store SDK, returning **complete user records from one endpoint**

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led a team of **6 interns** shipping an educational bot with NVIDIA NeMo guardrails and GPT-3.5-turbo, deployed in 8 courses reaching 60+ students each
- Built a Django REST API on PostgreSQL that grouped **300+ students** into cohorts by similarity of self-rated skill vectors
- Trained a scikit-learn resume classifier on 1,700+ records that held **88% accuracy** over six months in production
- Automated hiring workflows via the Lever API across two hiring cycles, saving **100+ hours per season**

### PROJECTS

**Who is Tyler Du, Portfolio Site with AI Agent** | github.com/Vicguin65/Portfolio-Website
*Personal project | Sept 2024 - Present*

- Built the full stack solo: React frontend, FastAPI on AWS Lambda, Terraform-managed infrastructure, and a **Claude agent** that evaluates fit against a pasted job description, grounding on a resume and knowledge base fetched from S3 at request time so content updates ship without a redeploy

### SKILLS & AWARDS

**Languages:** Python, Rust, TypeScript, JavaScript, HCL

**Cloud & Infrastructure:** AWS (Lambda, DynamoDB, EC2, S3, IAM), GCP, Azure, Cloudflare, Terraform, Docker, GitLab CI/CD

**Frameworks & Tools:** React, FastAPI, Django, PostgreSQL, Tauri, Git, Claude Code, Claude API, scikit-learn

**Certifications & Awards:** AWS Certified Cloud Practitioner, HashiCorp Terraform Associate, GIAC GFACT, Dean's Honor List
