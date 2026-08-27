<!-- company: Twitch -->

# Software Engineer I, Commerce Engineering at Twitch

*Tailored from `twitch.md` | Match: **Partial***

Tyler has a CS degree, strong AWS and full-stack fundamentals (React/TypeScript frontends, Python REST APIs on Lambda, PostgreSQL), and has shipped small consumer-facing products end to end, which maps reasonably onto the generalist product engineering expectations of a Software Engineer I. However, his professional depth is in cloud infrastructure and platform automation rather than consumer product surfaces, and the knowledge base shows no Golang, no mobile development, no DynamoDB/SQS/Step Functions/ECS, and no work on systems serving millions of concurrent users or on payments/commerce flows. The fit is plausible for an entry-level product engineering role but he would be learning Twitch's core stack and scale domain on the job.

---

## Tyler Du

Reno, NV | tyleryeedu@gmail.com | whoistylerdu.com  
linkedin.com/in/tyler-du-link | github.com/Vicguin65  

### WORK EXPERIENCE

**Zero Sum Defense** | Minneapolis, MN
*Member of Technical Staff | July 2025 - Present*

- Engineered and deployed the Actualize platform across **AWS**, **GCP**, **Azure**, and **Cloudflare**, ensuring high availability and cross-provider compatibility
- Automated provisioning of **50+ AWS accounts daily** for scalable, consistent infrastructure deployment
- Designed a scheduled health checker that has each tenant validate its configuration against a source-of-truth API weekly and self-correct, eliminating drift across single-tenant deployments

**AI Camp** | Palo Alto, CA
*Software Engineer Intern | Jan 2023 - Dec 2023*

- Developed **REST APIs** over a **PostgreSQL** database with a survey-similarity grouping algorithm, improving grouping efficiency for **300+ students**
- Led a team of **6 interns** to ship **NVIDIA NeMo** guardrails with **GPT-3.5-turbo** for an educational **Python**/Colang bot used in **8 courses** with **60+ students** each


### PROJECTS

**Who is Tyler Du, Portfolio + AI Agent | React, FastAPI, AWS Lambda, Terraform**
*Full-stack Engineer | Sept 2024 - Present*

- Built the full stack solo: **React 18 + Vite** frontend and **Python FastAPI** backend on **AWS Lambda** via Mangum, with infrastructure managed in **Terraform**
- Integrated **Anthropic Claude** to evaluate candidate fit, served through **API Gateway**, **CloudFront**, and **S3**

**Accessible Routes Routing API | Rensselaer Polytechnic Institute | Python, Django, React**
*Fullstack Engineer | Aug 2023 - Nov 2024*

- Developed a **RESTful API** in **Python** and **Django** serving campus accessibility data (stairs, elevators, ramps) so mobility-impaired students get turn-by-turn routes
- Deployed frontend and backend with **Docker** on **AWS EC2**, configuring domain name and SSL certificates

**Dandy's World Discord Bot | Python, discord.py, AWS EC2**
*Solo Developer | Oct 2024*

- Shipped a community bot for a Roblox game in **3 days** that automates party, text, and voice channel creation through slash commands, running 24/7 on an **AWS EC2** t3.micro server


### SKILLS & AWARDS

**Languages:** Python, TypeScript, JavaScript, Java, C, C++, Rust, HCL

**Frameworks & Cloud:** React, FastAPI, Django, REST APIs, PostgreSQL, AWS (Lambda, API Gateway, EC2, S3, CloudFront, IAM), Terraform, Docker, CI/CD, Git, Linux

**Certifications:** AWS Cloud Practitioner, Terraform Associate | **Awards:** National Cyber Scholar with Honors, Dean's Honor List


### EDUCATION

**Rensselaer Polytechnic Institute** | Troy, NY
*Bachelor of Science: Computer Science | GPA: 3.6 | May 2025*

- Relevant Coursework: Data Structures, Algorithms, Software Design and Documentation, Distributed Systems

---

## Tailoring Notes

- Led with work experience but rewrote Zero Sum Defense bullets to stress scalable systems design (self-healing tenant health checker) rather than pure cloud ops, since the role wants scalable application engineering.
- Promoted the portfolio site and Accessible Routes projects to the top of PROJECTS because they are the closest evidence of consumer-facing React/TypeScript plus API product work.
- Kept the Dandy's World Discord bot to show a shipped consumer product for a gaming community, which speaks to the gaming/streaming passion bonus point.
- Cut the IBM Identity Store API and IBM Terraform automation projects: both are internal infrastructure tooling and did not compete for space against consumer-facing work.
- Highlighted the grouping algorithm behind the AI Camp REST APIs to speak to the algorithms, data structures, and schema design requirement.
- Trimmed coursework and skills lines to keep the resume to one page.

## Knowledge Base Gaps

The knowledge base has no evidence for the following. Answer these and add them to `knowledge_base.md` so future tailoring can draw on them.

### Golang, a core part of Twitch's backend stack  `important`

Have you written any Go, in a class, side project, or at work? If so, what did you build with it and how large was the codebase?

### Systems handling millions of concurrent users  `blocking`

What is the highest traffic system you have worked on (requests per second, concurrent users, or daily active users), and what specifically did you do to make it handle that load?

### Consumer-facing product work that users love, with product metrics  `blocking`

For any product you shipped to real end users (portfolio site, Discord bot, Accessible Routes), what usage numbers can you cite: number of users, servers installed, sessions, or retention over time?

### Commerce, payments, subscriptions, or virtual currency systems  `important`

Have you built anything touching payments, billing, subscriptions, or virtual currency/credits, including test integrations with Stripe or similar? What flows did you implement and how did you handle failures or idempotency?

### Mobile development, native or hybrid  `nice-to-have`

Have you built any mobile app or mobile web experience (React Native, Swift, Kotlin, or responsive mobile-first web)? What did it do and did it reach users?

### AWS DynamoDB, SQS, Step Functions, ECS  `important`

Which of DynamoDB, SQS, Step Functions, or ECS have you used in a real deployment, and what was the workload (table access patterns, queue volume, container services) you ran on them?

### Schema design and data modeling depth  `important`

Describe a database schema you designed yourself: what entities and relationships, how many tables, and what tradeoffs did you make on indexing, normalization, or access patterns?

### Cross-team collaboration and communication in a large product organization  `important`

Give a concrete example of shipping something that required agreement across multiple teams or stakeholders: who was involved, what you negotiated, and how the feature landed.

### Turning customer feedback into features, experimentation and A/B testing  `nice-to-have`

Have you ever changed a product based on user feedback or run an experiment/feature flag rollout? What was the feedback, what did you build in response, and what changed afterward?

### Frontend testing and modern frontend engineering practices  `nice-to-have`

What testing and tooling do you use on your React/TypeScript work (Jest, Vitest, Playwright, component libraries, state management), and on which project did you set it up?

