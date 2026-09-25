<!-- company: Platform Infrastructure -->

# Platform & Infrastructure Engineer

*Hand-authored, not produced by `tailor_resume.py`. Targets platform, infrastructure, cloud, and DevOps roles generally rather than one specific job description. Rebuild the PDF with `render_resume.py platform-infrastructure.md`.*

---

## Tyler Du

Platform & Infrastructure Engineer
Reno, NV | (775) 997-8654 | tyleryeedu@gmail.com | whoistylerdu.com
linkedin.com/in/tyler-du-link | github.com/Vicguin65

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Distributed Systems and Algorithms, Data Structures, Algorithms, Ethical Hacking

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN (Remote)
*Member of Technical Staff | July 2025 - Present*

- Built the AWS account provisioning pipeline behind customer signup for the **Actualize** identity platform, replacing a **25-minute** manual setup per account with a zero-touch flow that has provisioned nearly **20,000 accounts** at **50+ a day**
- Designed a self-healing drift checker, a weekly **EventBridge** job that reconciles each tenant against its expected state; it caught **200+ misconfigured tenants** on its first run while preserving single-tenancy's blast-radius isolation
- Deployed Actualize across **AWS**, **GCP**, **Azure**, and **Cloudflare**, standardizing multi-cloud infrastructure with shared **Terraform** modules
- Built the autoscaling fleet of ephemeral Windows **EC2** **GitLab** runners in **Terraform** that the desktop client's Windows builds run on, and maintained the Windows x64 build job
- Owned native binary packaging for hardware-token authentication in the **Rust** and **Tauri** desktop client, writing the per-target build scripts **GitLab CI** runs for Windows, macOS, and Linux so a bad binary surfaces in CI, not on user machines
- Use **Claude Code** daily for infrastructure automation and platform engineering, scoping and reviewing agent-generated changes before they ship

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Automated provisioning of an AWS **VPC** with public and private subnets and 4 EC2 servers via **HCP Terraform**, including automated deployment of application updates for the IBM Cloud team
- Built an open-source **REST API** for the AWS Identity Store on **Lambda** and **CloudFormation**, serving **100+ IBM teams** daily and integrated with IBM Security Verify for single sign-on

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led a team of **6 interns** shipping a production LLM feature deployed in **8 courses** reaching **60+ students** each
- Automated hiring workflows via the Lever API across two hiring cycles, saving **100+ hours per season**

### PROJECTS

**Who is Tyler Du, Portfolio Site | Terraform, AWS Lambda, CloudFront, FastAPI** | github.com/Vicguin65/Portfolio-Website
*Personal project | Sept 2024 - Present*

- Provisioned the entire stack in **Terraform**: **S3** and **CloudFront** frontend, **FastAPI** on **AWS Lambda** behind **API Gateway**, with **Route53**, **ACM**, and **SES**
- Automated release with a deploy script that builds, syncs to S3, and invalidates CloudFront

### SKILLS & AWARDS

**Cloud & Infrastructure:** AWS (Lambda, API Gateway, EC2, S3, DynamoDB, IAM, EventBridge, CloudFormation, Route53, ACM, SES), GCP, Azure, Cloudflare

**Infrastructure as Code & Tooling:** Terraform, HCP Terraform, GitLab CI/CD, Docker, Git, Linux, Claude Code

**Languages:** Python, Rust, HCL, TypeScript, JavaScript

**Certifications & Awards:** AWS Certified Cloud Practitioner, HashiCorp Terraform Associate, GIAC GFACT; National Cyber Scholar with Honors, Dean's Honor List

---

## Tailoring Notes

*Refreshed 2026-09-25 against the knowledge base as of 2026-09-21 and the current base resume.*

- Added a title line under the name, which the base resume deliberately omits. It earns its place here because the target role type is narrow.
- Brought the two lead bullets up to the base resume's wording and metrics: nearly 20,000 accounts provisioned (19,889 as of 2026-09-15) and 200+ misconfigured tenants caught on the drift checker's first run.
- Added the ephemeral Windows EC2 GitLab runner autoscaler (Terraform, March 2026). It is the most purely platform-engineering item in the knowledge base and was missing entirely.
- Fixed an overclaim. The old bullet said Tyler owned the client's "build pipeline"; the knowledge base is explicit that the Tauri CI pipeline was a teammate's. The bullet now claims only the per-target build scripts GitLab CI runs, plus the Windows x64 build job.
- Dropped "automated CI/CD pipelines" from the multi-cloud bullet for the same reason: the knowledge base no longer carries a general CI/CD pipeline claim. "CI/CD" in skills is now "GitLab CI/CD", which it does support.
- Added DynamoDB to skills (the knowledge base now calls it Tyler's strongest database, used for the tenant table).
- Dropped Java, C, and C++ from languages, matching the base resume. The knowledge base still has nothing behind them.
- Marked Zero Sum Defense "(Remote)" and gave the portfolio project its GitHub link and "Personal project" label, matching the base resume.
- Reordered the IBM entry to lead with the Terraform and VPC automation, and trimmed AI Camp to leadership plus the Lever metric, as before.

## Knowledge Base Gaps

- Kubernetes: listed on an older resume, still undocumented in the knowledge base, and commonly screened for in platform roles.
- Observability and monitoring: no evidence of Prometheus, Grafana, Datadog, CloudWatch dashboards, or alerting design.
- Incident response and on-call: no on-call rotation, postmortem, or production incident experience recorded.
- Secrets management: Vault and similar tooling are not documented.
- Docker: listed in skills on every resume, but the knowledge base entry is still a TODO. What was it used for?
- Runner autoscaler scale: how many runners at peak, and what did it replace (a static runner, a hosted runner, build time or cost saved)? A number here would make the bullet much stronger.
