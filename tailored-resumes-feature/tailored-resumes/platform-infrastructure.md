<!-- company: Platform Infrastructure -->

# Platform & Infrastructure Engineer

*Hand-authored, not produced by `tailor_resume.py`. Targets platform, infrastructure, cloud, and DevOps roles generally rather than one specific job description. Rebuild the PDF with `render_resume.py platform-infrastructure.md`.*

---

## Tyler Du

Platform & Infrastructure Engineer
Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com
linkedin.com/in/tyler-du-link | github.com/Vicguin65

### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Distributed Systems and Algorithms, Data Structures, Algorithms, Ethical Hacking

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Built the AWS account provisioning pipeline behind customer signup for the **Actualize** identity platform, automating a **25-minute** manual setup and supporting **50+ accounts daily**
- Designed a self-healing health checker running weekly on **EventBridge**, auditing each tenant's configuration against expected state and correcting drift automatically
- Engineered and deployed Actualize across **AWS**, **GCP**, **Azure**, and **Cloudflare**, standardizing provisioning with reusable **Terraform** modules and automated **CI/CD** pipelines
- Own the cross-platform native binary packaging and build pipeline for the **Rust** and **Tauri** desktop client, catching per-target mismatches at build time rather than on user machines
- Use **Claude Code** daily for infrastructure automation and platform engineering, scoping and reviewing agent-generated changes before they ship

**IBM** | Troy, NY
*Software Engineering Intern | Jan 2024 - Aug 2024*

- Automated provisioning of an AWS **VPC** with public and private subnets and 4 EC2 servers via **HCP Terraform**, including automated deployment of application updates for the IBM Cloud team
- Built an open-source **REST API** for the AWS Identity Store on **Lambda** and **CloudFormation**, serving **100+ IBM teams** daily and integrated with IBM Security Verify for single sign-on

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | May 2022 - Dec 2023*

- Led a team of **6 interns** shipping a production LLM feature deployed in **8 courses** reaching **60+ students** each
- Automated hiring workflows via the Lever API, saving **100+ hours per hiring season**

### PROJECTS

**Who is Tyler Du, Portfolio Site | Terraform, AWS Lambda, CloudFront, FastAPI**
*Full-Stack Engineer | Sept 2024 - Present*

- Provisioned the entire stack in **Terraform**: **S3** and **CloudFront** frontend, **FastAPI** on **AWS Lambda** behind **API Gateway**, with **Route53**, **ACM**, and **SES**
- Automated release with a deploy script that builds, syncs to S3, and invalidates CloudFront

### SKILLS & AWARDS

**Cloud & Infrastructure:** AWS (Lambda, API Gateway, EC2, S3, IAM, EventBridge, CloudFormation, Route53, ACM, SES), GCP, Azure, Cloudflare

**Infrastructure as Code & Tooling:** Terraform, HCP Terraform, Docker, CI/CD, Git, Linux, Claude Code

**Languages:** Python, Rust, HCL, JavaScript, TypeScript, Java, C, C++

**Awards & Certifications:** AWS Certified Cloud Practitioner, HashiCorp Terraform Associate, GIAC Foundational Cybersecurity Technologies; National Cyber Scholar with Honors, Dean's Honor List

---

## Tailoring Notes

- Added a title line under the name, which the base resume deliberately omits. It earns its place here because the target role type is narrow.
- Led Zero Sum Defense with provisioning and drift remediation, the two bullets that read most directly as platform engineering.
- Reordered the IBM entry to lead with the Terraform and VPC automation rather than the identity API, and dropped the SCIM detail, which is an application-level story.
- Trimmed AI Camp to leadership plus the Lever automation metric, dropping its API and machine learning detail as the least relevant experience for this role type.
- Reframed the portfolio site around its Terraform-managed AWS footprint and release automation instead of its AI agent.
- Cut Accessible Routes. Its Docker and EC2 deployment work is infrastructure-relevant, but it is a school project that never reached production and the space went to current work instead.
- Restored Route53, ACM, SES, CloudFormation, EventBridge, and Linux to the skills block, all of which the base resume drops for space.

## Knowledge Base Gaps

- Kubernetes: listed on an older resume, still undocumented in the knowledge base, and commonly screened for in platform roles.
- Observability and monitoring: no evidence of Prometheus, Grafana, Datadog, CloudWatch dashboards, or alerting design.
- Incident response and on-call: no on-call rotation, postmortem, or production incident experience recorded.
- Secrets management: Vault and similar tooling are not documented.
- Scale figures: total accounts and tenants under management are still unknown, which is the number platform interviews probe first.
