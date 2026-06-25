// projects data — single source of truth for the portfolio
const projects = [
  {
    title: '"Who is Tyler Du"',
    description:
      "This is the website before your very eyes! " +
      "As I near the end of my undergraduate education at RPI, I wanted to commemorate everything I've accomplished, " +
      "which is why I started this project. I'll do my best to keep this website as up-to-date as possible and to occasionally add fun, " +
      "curious features!",
    technologies: ["React", "FastAPI", "AWS"],
    codeLink: "https://github.com/Vicguin65/Portfolio-Website",
    startDate: new Date(2024, 8),
    endDate: new Date(),
  },
  {
    title: "Dandy's World Discord Bot",
    description:
      "Dandy's World Discord Bot is a Discord Bot built in 3 days using the discord.py library. " +
      "This bot is currently ran on a t3.micro Ubuntu server hosted on AWS. " +
      "Inspired by a game on Roblox, this bot automates the creation of parties, text channels, and voice channels through slash commands.",
    technologies: ["Python", "AWS EC2"],
    codeLink: "https://github.com/Vicguin65/Dandy-World-Discord-Bot",
    startDate: new Date(2024, 9, 16),
    endDate: new Date(2024, 9, 19),
  },
  {
    title: "Accessible Routes",
    description:
      "Accessible Routes was a website worked on during Fall 2023 and Spring 2024. " +
      "Using RPI's accessibility data, I created a backend API that provided the accessible routes between buildings on campus.",
    technologies: ["React", "Django", "CSS", "AWS EC2"],
    codeLink: "https://github.com/Accessible-Routes",
    startDate: new Date(2023, 8),
    endDate: new Date(2024, 10, 16),
  },
  {
    title: "REST API For AWS Identity Store",
    description:
      "An open-source REST API wrapper built in collaboration with IBM's cloud team to address critical gaps in the AWS IAM Identity Center SCIM API. " +
      "The native AWS SDK lacked pagination support and left several IAM workflows inaccessible, blocking enterprise identity management at scale. " +
      "The wrapper fills those gaps with a clean REST interface, deployed on AWS Lambda behind API Gateway with infrastructure provisioned via AWS SAM and Terraform.",
    technologies: [
      "Python",
      "AWS Lambda",
      "AWS API Gateway",
      "AWS SAM",
      "Terraform",
    ],
    codeLink: "https://github.com/Vicguin65/IBM-Identity-Center-API",
    startDate: new Date(2024, 0),
    endDate: new Date(2024, 4),
  },
  {
    title: "Terraform Automation For Data Science App",
    description:
      "A collaborative RCOS project mentored by an IBM Principal Cloud Architect. " +
      "Three commands (init, plan, apply) are all it takes to provision a full AWS Virtual Private Cloud: " +
      "2 public subnets, 2 private subnets, and 4 t2.large Ubuntu servers hosting a React data science application " +
      "analyzing polygraph test accuracy. Built with four students over Summer 2024 using Terraform CDK for infrastructure-as-code.",
    technologies: ["HCP Terraform CDK", "AWS VPC", "React"],
    codeLink: "https://github.com/Vicguin65/IBM-Terraform-Automation",
    startDate: new Date(2024, 4),
    endDate: new Date(2024, 7),
  },
  {
    title: "Grouping API for Camp Students",
    description:
      "Using REST API standards and the Django framework, I wrote APIs to model groups of students based on surveys in a PostgreSQL database. " +
      "A grouping algorithm matches students with the most similarity. Analyzed data for about 300 students in 2023.",
    technologies: ["Python", "Django", "PostgreSQL"],
    startDate: new Date(2023, 0),
    endDate: new Date(2023, 3),
  },
  {
    title: "Hiring Management System Automation",
    description:
      "Using Lever's API, parts of the hiring flow were automated saving over 100 hours per hiring season. " +
      "Trained an AI model using scikit-learn to evaluate resumes, built on over 1,700 past candidate records with 88% accuracy over its first six months.",
    technologies: ["Python", "Scikit-Learn", "AWS S3"],
    startDate: new Date(2022, 4),
    endDate: new Date(2022, 7),
  },
  {
    title: "School Contacts Webscrape",
    description:
      "Developed an application to collect school contact information via web scraping. " +
      "Over 68,000 faculty member records were collected using BeautifulSoup4, Selenium, and the OpenAI gpt-3.5-turbo API.",
    technologies: ["Python", "BeautifulSoup4", "Selenium", "GPT-3.5-turbo"],
    startDate: new Date(2023, 5),
    endDate: new Date(2023, 6),
  },
  {
    title: "git-remote-gcs",
    description:
      "An open-source Python tool that enables Google Cloud Storage to function as a serverless Git remote repository, " +
      "bringing GCS parity with git-remote-s3 without requiring VMs or managed services. " +
      "Features native GCP IAM integration for access control, branch protection to prevent force-pushes, " +
      "per-reference locking to prevent concurrent push conflicts, and customer-managed encryption key (CMEK) support. " +
      "Distributed via PyPI and compatible with macOS, Linux, and Windows using standard gcs:// remote URLs.",
    technologies: ["Python", "Google Cloud Storage", "GCP IAM", "PyPI"],
    codeLink: "https://github.com/Vicguin65/git-remote-gcs",
    startDate: new Date(2026, 1),
    endDate: new Date(2026, 3),
  },
  {
    title: "Best Sun (HackRPI 2025)",
    description:
      "A solar panel feasibility assessment tool built at HackRPI 2025. " +
      "Given a location, the app queries the Google Places and Google Solar APIs to project energy output, " +
      "estimate cost savings, and calculate environmental impact such as carbon offsets. " +
      "Built in TypeScript and React with a focus on surfacing actionable insights from complex API responses.",
    technologies: [
      "React",
      "TypeScript",
      "Google Places API",
      "Google Solar API",
    ],
    codeLink: "https://github.com/Vicguin65/HackRPI2025",
    startDate: new Date(2025, 10, 8),
    endDate: new Date(2025, 10, 9),
  },
];

// Returns a human-readable duration string between two dates
const diff_text = (dt1, dt2) => {
  const diff_ms = Math.abs(dt2.getTime() - dt1.getTime()) / 1000;
  let diff_days = diff_ms / (60 * 60 * 24);
  let diff_months = 0;
  let diff_years = 0;

  if (diff_days > 30) {
    diff_months = diff_days / 30;
    diff_days = diff_days % 30;
  }
  if (diff_months > 12) {
    diff_years = diff_months / 12;
    diff_months = diff_months % 12;
  }

  diff_years = Math.round(diff_years);
  diff_months = Math.round(diff_months);
  diff_days = Math.round(diff_days);

  const parts = [];
  if (diff_years > 0)
    parts.push(`${diff_years} yr${diff_years > 1 ? "s" : ""}`);
  if (diff_months > 0) parts.push(`${diff_months} mo`);
  if (diff_days > 0) parts.push(`${diff_days} d`);
  return parts.join(", ");
};

const MONTHS = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const date_string = (dt) =>
  `${MONTHS[dt.getMonth()]} ${dt.getDate()}, ${dt.getFullYear()}`;

const same_date = (d1, d2) =>
  d1.getFullYear() === d2.getFullYear() &&
  d1.getMonth() === d2.getMonth() &&
  d1.getDate() === d2.getDate();

export { projects, diff_text, date_string, same_date };
