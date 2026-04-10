// projects data — single source of truth for the portfolio
const projects = [
  {
    title: '"Who is Tyler Du"',
    description:
      'This is the website before your very eyes! ' +
      'As I near the end of my undergraduate education at RPI, I wanted to commemorate everything I\'ve accomplished, ' +
      'which is why I started this project. I\'ll do my best to keep this website as up-to-date as possible and to occasionally add fun, ' +
      'curious features!',
    technologies: ['React', 'FastAPI', 'AWS'],
    codeLink: 'https://github.com/Vicguin65/Portfolio-Website',
    startDate: new Date(2024, 8),
    endDate: new Date(),
  },
  {
    title: "Dandy's World Discord Bot",
    description:
      "Dandy's World Discord Bot is a Discord Bot built in 3 days using the discord.py library. " +
      'This bot is currently ran on a t3.micro Ubuntu server hosted on AWS. ' +
      'Inspired by a game on Roblox, this bot automates the creation of parties, text channels, and voice channels through slash commands.',
    technologies: ['Python', 'AWS EC2'],
    codeLink: 'https://github.com/Vicguin65/Dandy-World-Discord-Bot',
    startDate: new Date(2024, 9, 16),
    endDate: new Date(2024, 9, 19),
  },
  {
    title: 'Accessible Routes',
    description:
      'Accessible Routes was a website worked on during Fall 2023 and Spring 2024. ' +
      "Using RPI's accessibility data, I created a backend API that provided the accessible routes between buildings on campus.",
    technologies: ['React', 'Django', 'CSS', 'AWS EC2'],
    codeLink: 'https://github.com/Accessible-Routes',
    startDate: new Date(2023, 8),
    endDate: new Date(2024, 10, 16),
  },
  {
    title: 'REST API For AWS Identity Store',
    description:
      'This was a project worked on during Spring 2024. An open-source project in collaboration with IBM\'s cloud team.',
    technologies: ['Python', 'AWS Lambda', 'AWS CloudFormation'],
    codeLink: 'https://github.com/Vicguin65/IBM-Identity-Center-API',
    startDate: new Date(2024, 0),
    endDate: new Date(2024, 4),
  },
  {
    title: 'Terraform Automation For Data Science App',
    description:
      'Terraform Automation was a project that ran during Summer 2024. ' +
      'Started with three other students, it automatically launches an AWS Virtual Private Cloud containing 2 public subnets, ' +
      '2 private subnets, and 4 total t2.large Ubuntu servers hosting a data science application about the accuracy of polygraph tests.',
    technologies: ['HCP Terraform CDK', 'AWS VPC', 'React'],
    codeLink: 'https://github.com/Vicguin65/IBM-Terraform-Automation',
    startDate: new Date(2024, 4),
    endDate: new Date(2024, 7),
  },
  {
    title: 'Grouping API for Camp Students',
    description:
      'Using REST API standards and the Django framework, I wrote APIs to model groups of students based on surveys in a PostgreSQL database. ' +
      'A grouping algorithm matches students with the most similarity. Analyzed data for about 300 students in 2023.',
    technologies: ['Python', 'Django', 'PostgreSQL'],
    startDate: new Date(2023, 0),
    endDate: new Date(2023, 3),
  },
  {
    title: 'Hiring Management System Automation',
    description:
      "Using Lever's API, parts of the hiring flow were automated saving over 100 hours per hiring season. " +
      'Trained an AI model using scikit-learn to evaluate resumes, built on over 1,700 past candidate records with 88% accuracy over its first six months.',
    technologies: ['Python', 'Scikit-Learn', 'AWS S3'],
    startDate: new Date(2022, 4),
    endDate: new Date(2022, 7),
  },
  {
    title: 'School Contacts Webscrape',
    description:
      'Developed an application to collect school contact information via web scraping. ' +
      'Over 68,000 faculty member records were collected using BeautifulSoup4, Selenium, and the OpenAI gpt-3.5-turbo API.',
    technologies: ['Python', 'BeautifulSoup4', 'Selenium', 'GPT-3.5-turbo'],
    startDate: new Date(2023, 5),
    endDate: new Date(2023, 6),
  },
];

// Returns a human-readable duration string between two dates
const diff_text = (dt1, dt2) => {
  const diff_ms  = Math.abs(dt2.getTime() - dt1.getTime()) / 1000;
  let diff_days   = diff_ms / (60 * 60 * 24);
  let diff_months = 0;
  let diff_years  = 0;

  if (diff_days > 30) {
    diff_months = diff_days / 30;
    diff_days   = diff_days % 30;
  }
  if (diff_months > 12) {
    diff_years  = diff_months / 12;
    diff_months = diff_months % 12;
  }

  diff_years  = Math.round(diff_years);
  diff_months = Math.round(diff_months);
  diff_days   = Math.round(diff_days);

  const parts = [];
  if (diff_years  > 0) parts.push(`${diff_years} yr${diff_years  > 1 ? 's' : ''}`);
  if (diff_months > 0) parts.push(`${diff_months} mo`);
  if (diff_days   > 0) parts.push(`${diff_days} d`);
  return parts.join(', ');
};

const MONTHS = [
  'January','February','March','April','May','June',
  'July','August','September','October','November','December',
];

const date_string = (dt) =>
  `${MONTHS[dt.getMonth()]} ${dt.getDate()}, ${dt.getFullYear()}`;

const same_date = (d1, d2) =>
  d1.getFullYear() === d2.getFullYear() &&
  d1.getMonth()    === d2.getMonth()    &&
  d1.getDate()     === d2.getDate();

export { projects, diff_text, date_string, same_date };
