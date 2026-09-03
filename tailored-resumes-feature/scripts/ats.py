#!/usr/bin/env python3
"""Score a resume the way an applicant tracking system does: by matching strings.

Most resumes are filtered before a human reads them, by software that does not read
either. It looks for the job description's own words. This module pulls those words out
of a description, ranks them by how hard the description leans on them, and reports which
ones a resume actually contains.

tailor_resume.py feeds the ranked list into the prompt and re-asks when a draft misses
something critical. render_resume.py re-checks a hand-edited resume against it. It also
runs standalone, to audit a resume that already exists:

    python tailored-resumes-feature/scripts/ats.py solace.md
    python tailored-resumes-feature/scripts/ats.py solace.md --resume Du_Tyler_Resume_Base.pdf

Nothing here calls a model. An ATS is a string matcher, so the check is a string matcher.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

FEATURE_ROOT = Path(__file__).resolve().parent.parent

# Terms an ATS is likely to have on a requisition, grouped so the report reads in an
# order a person can scan. Values are extra spellings that count as the same term.
SKILLS: dict[str, dict[str, tuple[str, ...]]] = {
    "languages": {
        "Python": (), "Rust": (), "Go": ("golang",), "JavaScript": (), "TypeScript": (),
        "Java": (), "C++": ("cpp",), "C#": ("csharp",), "Ruby": (), "PHP": (), "Swift": (),
        "Kotlin": (), "Scala": (), "Perl": (), "SQL": (), "HCL": (), "YAML": (),
        "Bash": ("shell scripting", "shell script"), "Node.js": ("nodejs",),
    },
    "cloud": {
        "AWS": ("amazon web services",), "GCP": ("google cloud",), "Azure": (),
        "Cloudflare": (), "Lambda": (), "EC2": (), "S3": (), "EKS": (), "ECS": (),
        "Fargate": (), "RDS": (), "DynamoDB": (), "CloudFormation": (), "CloudWatch": (),
        "API Gateway": (), "EventBridge": (), "VPC": (), "Route53": (), "SQS": (), "SNS": (),
        "CloudFront": (), "multi-cloud": ("multicloud",), "serverless": (),
    },
    "infrastructure": {
        "infrastructure": (), "cloud infrastructure": (),
        "Terraform": (), "OpenTofu": ("tofu",), "Kubernetes": ("k8s",), "Docker": (),
        "container": ("containerization", "containerized"), "Helm": (), "Ansible": (),
        "Pulumi": (), "Packer": (), "Nomad": (), "service mesh": (), "Istio": (),
        "Linux": (), "Unix": (), "command line": ("cli",), "networking": (), "DNS": (),
        "load balancing": ("load balancer",), "virtualization": ("virtual machine",),
        "bare metal": (), "homelab": ("home lab",), "self-hosted": ("self hosting",),
        "nginx": (), "systemd": (), "proxy": (),
        "infrastructure as code": ("iac",), "GitOps": (), "provisioning": (),
        "configuration management": (), "secrets management": (), "automation": ("automate",),
        "scripting": (),
    },
    "delivery": {
        "CI/CD": ("continuous integration", "continuous delivery", "continuous deployment"),
        "GitHub": (), "GitHub Actions": (), "Jenkins": (), "GitLab": (), "ArgoCD": (),
        "CircleCI": (), "Git": (), "Bazel": (), "release engineering": (),
    },
    "operations": {
        "on-call": ("oncall",), "incident response": ("incident management", "incident"),
        "postmortem": ("post mortem", "retrospective"), "root cause analysis": ("root cause",),
        "monitoring": ("monitor",), "observability": (), "logging": ("logs",), "tracing": (),
        "metrics": (), "alerting": ("alerts",), "Prometheus": (), "Grafana": (),
        "Datadog": (), "PagerDuty": (), "Splunk": (), "OpenTelemetry": (), "SLO": (),
        "SLA": (), "uptime": (), "reliability": ("reliable",), "resilience": ("resilient",),
        "anti-fragile": (), "high availability": (), "disaster recovery": (),
        "capacity planning": (), "troubleshooting": ("troubleshoot",),
        "debugging": ("debug",), "triage": (), "outage": (), "chaos engineering": (),
        "performance tuning": ("performance optimization",),
        "scalability": ("scalable", "scale"), "systems analysis": (),
        "architecture review": ("architectural review",), "architecture": (),
        "runbook": (), "failure modes": ("failure mode",),
    },
    "platform": {
        "platform engineering": ("platform engineer",),
        "internal developer platform": ("developer platform",),
        "developer experience": (), "developer tooling": ("tooling",),
        "self-service": (), "DevOps": (),
        "site reliability engineering": ("site reliability engineer", "sre"),
        "systems engineering": (), "distributed systems": (),
    },
    "data": {
        "PostgreSQL": ("postgres",), "MySQL": (), "Redis": (), "Kafka": (), "Snowflake": (),
        "Airflow": (), "Spark": (), "ETL": (), "data pipeline": (), "dbt": (),
        "MongoDB": (), "Elasticsearch": (), "BigQuery": (), "data engineering": ("data engineer",),
        "data modeling": (),
    },
    "application": {
        "React": (), "Next.js": (), "Vue": (), "Angular": (), "FastAPI": (), "Django": (),
        "Flask": (), "REST API": ("restful",), "API": (), "GraphQL": (), "gRPC": (),
        "microservices": ("microservice",), "event-driven": (), "message queue": (),
        "WebSocket": (), "frontend": ("front end",), "backend": ("back end",),
        "full stack": (), "caching": ("cache",), "concurrency": (),
    },
    "ai_ml": {
        "machine learning": (), "AI": ("artificial intelligence",),
        "LLM": ("large language model",),
        "RAG": ("retrieval augmented generation",), "PyTorch": (), "TensorFlow": (),
        "scikit-learn": ("sklearn",), "NLP": (), "prompt engineering": (),
        "fine-tuning": (), "vector database": (), "embeddings": (), "MLOps": (),
    },
    "security": {
        "OAuth": (), "SAML": (), "SSO": ("single sign on",), "SCIM": (), "IAM": (),
        "zero trust": (), "penetration testing": ("pentest",),
        "vulnerability": (), "encryption": ("encrypt",), "TLS": (), "compliance": (),
        "SOC 2": (), "threat modeling": (), "RBAC": (), "least privilege": (),
        "identity management": (), "security": ("cybersecurity",),
    },
    "practices": {
        "agile": (), "scrum": (), "code review": (), "unit testing": ("unit test",),
        "integration testing": (), "test automation": (), "pytest": (), "TDD": (),
        "documentation": (), "mentoring": ("mentor",), "cross-functional": (),
        "stakeholders": ("stakeholder",), "pair programming": (), "technical writing": (),
        "internship": ("intern",), "computer science": (), "bachelor": ("bachelors",),
    },
    "logistics": {
        "on-site": ("onsite", "in person"), "hybrid": (), "remote": (),
        "new grad": ("new graduate", "recent graduate", "entry level"),
        "relocation": ("relocate",),
    },
    "domain": {
        "healthcare": ("health care",), "fintech": (), "e-commerce": (), "EHR": (),
        "telehealth": (), "clinical": (), "patient": (), "HIPAA": (), "Medicare": (),
        "insurance": (), "startup": (), "Series A": (), "Series B": (), "Series C": (),
    },
    "traits": {
        "curiosity": ("curious",), "collaboration": ("collaborate",),
        "communication": ("communicate",), "problem solving": (),
        "attention to detail": (), "initiative": (), "urgency": (), "mission-driven": (),
    },
}

# Nothing in these can be earned by rewording a resume: an industry Tyler has not worked
# in, a personality the resume cannot assert, a commute. They are reported, and they count
# against the score the way a real matcher would count them, but they are never sent back
# to the model as something to work in.
REPORT_ONLY = {"domain", "traits", "logistics"}

# Matched case-sensitively, because the lowercase form is an ordinary English word.
CASED = {"Go", "AI"}

# Capitalised noise the novel-term scan would otherwise mistake for a skill.
GENERIC_STOP = {
    "US", "USA", "IT", "HR", "PTO", "EEO", "LGBTQ", "FAQ", "CEO", "CTO", "COO", "CFO",
    "VP", "OK", "AM", "PM", "LLC", "INC", "NYC", "SF", "PST", "EST", "Q1", "Q2", "Q3",
    "Q4", "401K", "PPO", "HMO", "OTE", "IPO", "LinkedIn", "GitHub", "Bloomberg",
    "Glassdoor", "Greenhouse", "Workday", "Series", "Capital", "Ventures", "Partners",
    "TechCrunch", "YouTube", "JavaScript", "TypeScript",
}

TIER_ORDER = ("critical", "important", "optional")
TIER_POINTS = {"critical": 5, "important": 3, "optional": 1}

# Headings that introduce the part of a description a requisition is built from. A block
# runs from one of these to the next heading of either kind.
REQ_HEADING_RE = re.compile(
    r"^#{0,4}\s*(?:about the role|the role|what you.{0,15}do|responsibilities|"
    r"what you.{0,15}bring.*|what we.{0,20}looking for.*|requirements|qualifications|"
    r"must[- ]have.*|nice[- ]to[- ]have.*|preferred.*|skills.*|experience.*|"
    r"what you.{0,15}learn|who you are|about you|sounds like you.*|you will.*|"
    r"your background.*)\s*:?\s*$",
    re.IGNORECASE,
)
END_HEADING_RE = re.compile(
    r"^#{0,4}\s*(?:about (?:us|the company|[A-Z].*)|benefits.*|compensation.*|salary.*|"
    r"perks.*|why join.*|our values.*|equal (?:employment )?opportunity.*|how to apply.*|"
    r"apply.*|interview process.*)\s*:?\s*$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Keyword:
    term: str
    category: str
    forms: tuple[str, ...]
    hits: int
    in_requirements: bool
    cased: bool = False

    @property
    def weight(self) -> int:
        """Frequency, plus a bump for landing where the requisition is written from."""
        return self.hits + (2 if self.in_requirements else 0)

    @property
    def tier(self) -> str:
        """How likely this term is to be a scored row on the requisition.

        Repetition is the signal. A description that says troubleshooting twice inside its
        requirements is describing the job; one that mentions Kubernetes once in a list of
        things you will learn is not the same claim.
        """
        if self.hits >= 3 or (self.hits >= 2 and self.in_requirements):
            return "critical"
        if self.hits == 2 or self.in_requirements:
            return "important"
        return "optional"

    @property
    def actionable(self) -> bool:
        return self.category not in REPORT_ONLY

    def found_in(self, text: str) -> bool:
        return any(_compile(f, self.cased).search(text) for f in self.forms)


@dataclass
class Coverage:
    keywords: list[Keyword]
    matched: list[Keyword]
    missing: list[Keyword]
    knockouts: list[str]

    @property
    def score(self) -> int:
        earned = sum(TIER_POINTS[k.tier] for k in self.matched)
        total = earned + sum(TIER_POINTS[k.tier] for k in self.missing)
        return round(100 * earned / total) if total else 100

    def by_tier(self, keywords: list[Keyword], tier: str) -> list[Keyword]:
        return [k for k in keywords if k.tier == tier]

    @property
    def targets(self) -> list[Keyword]:
        """Misses worth sending back to the model: real skills, not domain or personality."""
        return [k for k in self.missing if k.actionable and k.tier in ("critical", "important")]

    @property
    def unreachable(self) -> list[Keyword]:
        """Misses that cost score but that no rewording can honestly earn."""
        return [k for k in self.missing if not k.actionable]

    @property
    def needs_revision(self) -> bool:
        critical = [k for k in self.targets if k.tier == "critical"]
        return bool(critical) or len(self.targets) >= 3


@lru_cache(maxsize=None)
def _compile(alias: str, cased: bool = False) -> re.Pattern:
    """Match an alias tolerantly: 'on-call' also finds 'on call' and 'oncall'.

    Separators are optional, plurals and -ing/-ed forms count, and a match has to sit on a
    token boundary so 'Java' does not fire on 'JavaScript'.
    """
    parts = [p for p in re.split(r"[-\s/._]+", alias) if p]
    core = r"[-\s/._]?".join(re.escape(p) for p in parts)
    left = r"(?<![A-Za-z0-9])" if parts[0][0].isalnum() else ""
    right = ""
    if parts[-1][-1].isalnum():
        # 'troubleshoot' has to reach 'troubleshooters', which is how descriptions
        # usually say it. Short aliases are left alone: AWS must not match AWSes.
        tail = r"(?:s|es|ing|ed|er|ers|ors)?" if len(alias) >= 4 and alias[-1].isalpha() else ""
        right = tail + r"(?![A-Za-z0-9])"
    return re.compile(left + core + right, 0 if cased else re.IGNORECASE)


def _count(text: str, forms: tuple[str, ...], cased: bool) -> int:
    """Mentions of a term, counting overlapping spellings once.

    'homelab' and 'home lab' both match the same six letters, and a term that looked twice
    as frequent as it is would land a tier too high.
    """
    spans = sorted(m.span() for form in forms for m in _compile(form, cased).finditer(text))
    hits, reach = 0, -1
    for start, end in spans:
        if start >= reach:
            hits += 1
        reach = max(reach, end)
    return hits


def _requirements_text(jd_text: str) -> str:
    """The blocks of a description that state what the job needs, headings dropped."""
    blocks: list[str] = []
    collecting = False
    for line in jd_text.splitlines():
        stripped = line.strip()
        if REQ_HEADING_RE.match(stripped):
            collecting = True
            continue
        if END_HEADING_RE.match(stripped):
            collecting = False
            continue
        if collecting:
            blocks.append(line)
    return "\n".join(blocks) if blocks else jd_text


CAMEL_RE = re.compile(r"\b[A-Z][a-z]+(?:[A-Z][a-z0-9]+)+\b")
ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,5}\b")


def _novel_terms(jd_text: str, req_text: str, known: set[str]) -> list[Keyword]:
    """Catch product names the dictionary has never heard of, like a new tool or vendor.

    Held to a higher bar than dictionary terms: a single mention is almost always noise,
    and anything in the opening lines is the company or the job title, not a skill.
    """
    header = "\n".join(jd_text.splitlines()[:3])
    candidates: dict[str, int] = {}
    for match in list(CAMEL_RE.finditer(jd_text)) + list(ACRONYM_RE.finditer(jd_text)):
        token = match.group(0)
        if token.lower() in known or token in GENERIC_STOP or token in header:
            continue
        candidates[token] = candidates.get(token, 0) + 1

    return [
        Keyword(token, "other", (token,), hits, bool(_compile(token).search(req_text)))
        for token, hits in candidates.items()
        if hits >= 2
    ]


def extract_keywords(jd_text: str) -> list[Keyword]:
    """Every term in a description that a requisition could plausibly be built from."""
    req_text = _requirements_text(jd_text)
    keywords: list[Keyword] = []
    known: set[str] = set()

    for category, terms in SKILLS.items():
        for term, aliases in terms.items():
            forms = (term, *aliases)
            cased = term in CASED
            known.update(f.lower() for f in forms)
            hits = _count(jd_text, forms, cased)
            if not hits:
                continue
            in_req = any(_compile(f, cased).search(req_text) for f in forms)
            keywords.append(Keyword(term, category, forms, hits, in_req, cased))

    keywords += _novel_terms(jd_text, req_text, known)
    keywords.sort(key=lambda k: (TIER_ORDER.index(k.tier), -k.weight, k.category, k.term.lower()))
    return keywords


def resume_text(resume) -> str:
    """Flatten a resume into the plain string a parser would see."""
    if isinstance(resume, str):
        text = resume
    else:
        parts = [resume.header.name, *resume.header.contact_lines]
        for section in resume.sections:
            parts.append(section.heading)
            parts += section.lines
            for entry in section.entries:
                parts += [entry.title, entry.location, entry.subtitle, entry.dates, *entry.bullets]
        text = "\n".join(p for p in parts if p)
    return re.sub(r"^\s*[-*•●]\s*", "", text.replace("**", ""), flags=re.MULTILINE)


PHONE_RE = re.compile(r"(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
AUTH_RE = re.compile(r"authoriz|work authorization|citizen|permanent resident|no sponsorship", re.I)
JD_AUTH_RE = re.compile(r"must be based in|authorized to work|work authorization|sponsorship", re.I)
ONSITE_RE = re.compile(r"in[- ]person|on[- ]?site|hybrid|days a week|days per week|in the office", re.I)
OFFICE_RE = re.compile(r"in (?:our|the) ([A-Z][a-zA-Z.]+(?: [A-Z][a-zA-Z.]+){0,3}) office")
CITY_STATE_RE = re.compile(r"\b([A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+){0,2}),\s*([A-Z]{2})\b")


def knockouts(text: str, jd_text: str) -> list[str]:
    """Rules that reject a resume before a single keyword is scored."""
    problems = []
    if not PHONE_RE.search(text):
        problems.append("No phone number. Some parsers mark the profile incomplete and never rank it.")
    if not EMAIL_RE.search(text):
        problems.append("No email address in the contact block.")
    if JD_AUTH_RE.search(jd_text) and not AUTH_RE.search(text):
        problems.append(
            "The description raises work authorization and the resume says nothing about it. "
            "The field defaults to unknown, which strict filters read as needs sponsorship."
        )

    if ONSITE_RE.search(jd_text):
        jd_cities = {m.group(1) for m in OFFICE_RE.finditer(jd_text)}
        jd_cities |= {m.group(1) for m in CITY_STATE_RE.finditer(jd_text)}
        header = "\n".join(text.splitlines()[:4])
        mine = CITY_STATE_RE.search(header)
        if jd_cities and mine and mine.group(1) not in jd_cities and "relocat" not in text.lower():
            problems.append(
                f"Resume location reads {mine.group(0)} and the role is onsite in "
                f"{sorted(jd_cities)[0]}. Radius filters cut this before scoring. Say you "
                "are relocating, or leave the city off."
            )
    return problems


def analyze(jd_text: str, resume, keywords: list[Keyword] | None = None) -> Coverage:
    keywords = keywords if keywords is not None else extract_keywords(jd_text)
    text = resume_text(resume)
    matched = [k for k in keywords if k.found_in(text)]
    missing = [k for k in keywords if k not in matched]
    return Coverage(keywords, matched, missing, knockouts(text, jd_text))


def _names(keywords: list[Keyword], limit: int | None = None) -> str:
    shown = keywords if limit is None else keywords[:limit]
    text = ", ".join(k.term for k in shown)
    extra = len(keywords) - len(shown)
    return f"{text} (+{extra} more)" if extra > 0 else text


def format_report(coverage: Coverage, indent: str = "  ") -> str:
    """The console summary printed after a tailoring or a re-render."""
    counts = " | ".join(
        f"{tier} {len(coverage.by_tier(coverage.matched, tier))}/"
        f"{len(coverage.by_tier(coverage.keywords, tier))}"
        for tier in TIER_ORDER
    )
    lines = [f"{indent}ATS keyword coverage: {coverage.score}/100  ({counts})"]
    for tier in ("critical", "important"):
        missed = [k for k in coverage.by_tier(coverage.missing, tier) if k.actionable]
        if missed:
            lines.append(f"{indent}  Missing {tier}: {_names(missed, 12)}")
    if coverage.unreachable:
        lines.append(f"{indent}  Out of reach: {_names(coverage.unreachable, 8)}")
    for problem in coverage.knockouts:
        lines.append(f"{indent}  Knockout: {problem}")
    return "\n".join(lines)


def markdown_section(coverage: Coverage) -> list[str]:
    """The coverage section appended to a tailored resume's Markdown file."""
    counts = ", ".join(
        f"{tier} {len(coverage.by_tier(coverage.matched, tier))} of "
        f"{len(coverage.by_tier(coverage.keywords, tier))}"
        for tier in TIER_ORDER
    )
    lines = [
        "## ATS Keyword Coverage",
        "",
        "How much of this description's own vocabulary the resume repeats back, scored the "
        "way a keyword matcher would. Terms are ranked by how often the description uses "
        "them and whether they appear in its requirements.",
        "",
        f"**Score: {coverage.score}/100** ({counts})",
        "",
    ]
    for tier in TIER_ORDER:
        missed = [k for k in coverage.by_tier(coverage.missing, tier) if k.actionable]
        if missed:
            lines += [f"**Missing, {tier}:** {_names(missed)}", ""]
    if coverage.matched:
        lines += [f"**Matched:** {_names(coverage.matched)}", ""]
    if coverage.unreachable:
        lines += [
            f"**Out of reach:** {_names(coverage.unreachable)}",
            "",
            "These cost score and no rewording earns them: an industry Tyler has not worked "
            "in, a personality a resume cannot assert, a commute.",
            "",
        ]
    if coverage.knockouts:
        lines += ["**Knockout risks**", ""]
        lines += [f"- {p}" for p in coverage.knockouts]
        lines.append("")
    lines.append(
        "A missing term is only worth fixing if the knowledge base can back it up. The rest "
        "belong in the gaps above, not in the resume."
    )
    return lines


PROMPT_BLOCK = """\

== ATS Keywords ==

Software will scan this resume for literal strings before a person reads it. These terms \
came out of the job description, ranked by how hard it leans on them:

{tiers}
Where the sources support a term, use the job description's word for it. If Tyler built \
drift correction and the description says monitoring, write monitoring. Where the sources \
do not support a term, leave it out and record it in knowledge_gaps: a keyword he cannot \
defend in an interview is worse than a miss. Never add a skills-section entry for a tool \
he has not used.\
"""


def prompt_block(keywords: list[Keyword]) -> str:
    """The keyword brief handed to the model alongside the job description."""
    actionable = [k for k in keywords if k.actionable]
    labels = {"critical": "Critical", "important": "Important", "optional": "Also scanned"}
    tiers = []
    for tier in TIER_ORDER:
        terms = [k for k in actionable if k.tier == tier]
        if terms:
            tiers.append(f"{labels[tier]}: {_names(terms, 30)}")
    if not tiers:
        return ""
    return PROMPT_BLOCK.format(tiers="\n".join(tiers) + "\n")


REVISION = """\

Your previous draft missed these keywords from the description: {terms}. Work in the ones \
the sources genuinely support, by rewording bullets you already have rather than adding \
new ones. Leave out any the sources do not support and record those as knowledge gaps \
instead.\
"""


def revision_instruction(targets: list[Keyword]) -> str:
    return REVISION.format(terms=_names(targets, 10)) if targets else ""


def _read_resume(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        from pypdf import PdfReader

        return "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)

    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".md":
        # Read only the resume body. Tailoring notes and gap questions name the very
        # keywords being scored, and counting those would flatter every resume.
        from render_resume import ParseError, _resume_body

        try:
            return "\n".join(_resume_body(text))
        except ParseError:
            return text
    return text


def _resolve(jd: str) -> Path:
    path = Path(jd)
    if path.exists():
        return path
    for suffix in ("", ".md", ".txt"):
        candidate = FEATURE_ROOT / "job-descriptions" / f"{path.name}{suffix}"
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"No such job description: {jd}")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("jd", help="A job description. A bare name resolves inside job-descriptions/.")
    parser.add_argument("--resume", type=Path, help="A .pdf or .md resume. Defaults to this job's tailored Markdown, then the base PDF.")
    parser.add_argument("--all", action="store_true", help="List every extracted keyword, matched and missed.")
    args = parser.parse_args()

    try:
        jd_path = _resolve(args.jd)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1

    out_dir = FEATURE_ROOT / "tailored-resumes"
    if args.resume:
        candidates = [args.resume, out_dir / args.resume.name]
    else:
        candidates = [out_dir / f"{jd_path.stem}.md", out_dir / "Du_Tyler_Resume_Base.pdf"]
    resume_path = next((p for p in candidates if p.exists()), None)
    if resume_path is None:
        print(f"No resume found. Looked for: {', '.join(str(c) for c in candidates)}", file=sys.stderr)
        return 1

    jd_text = jd_path.read_text(encoding="utf-8")
    coverage = analyze(jd_text, _read_resume(resume_path))

    print(f"Job description: {jd_path.name}")
    print(f"Resume:          {resume_path.name}\n")
    print(format_report(coverage, indent=""))

    if args.all:
        print()
        for tier in TIER_ORDER:
            for keyword in coverage.keywords:
                if keyword.tier != tier:
                    continue
                mark = "OK  " if keyword in coverage.matched else "MISS"
                flag = "  (report only)" if not keyword.actionable else ""
                print(f"  {mark} [{tier:<9}] {keyword.term:<28} jd hits: {keyword.hits}{flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
