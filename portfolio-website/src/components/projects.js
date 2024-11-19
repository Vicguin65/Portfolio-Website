// projects data
const projects = [
  {
    title: '"Who is Tyler Du"',
    description:
      "This is the website before your very eyes! " +
      "As I near the end of my undergraduate education at RPI, I wanted to commemorate everything I've accomplished, " +
      "which is why I started this project. I'll do my best to keep this website as up-to-date as possible and to occasionally add fun, " +
      "curious features!",
    technologies: ["React"],
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
    technologies: ["Python"],
    codeLink: "https://github.com/Vicguin65/Dandy-World-Discord-Bot",
    startDate: new Date(2024, 9, 16),
    endDate: new Date(2024, 9, 19),
  },
  {
    title: "Accessible Routes",
    description:
      "Accessible Routes was a website that was worked on during Fall 2023 and Spring 2024. " +
      "Using RPI's accessibility data, I created a backend API that provided the accessible routes between buildings on campus.",
    technologies: ["React", "Django", "CSS", "AWS EC2"],
    codeLink: "https://github.com/Accessible-Routes",
    startDate: new Date(2023, 8),
    endDate: new Date(2024, 10, 16),
  },
  {
    title: "REST API For AWS Identity Store",
    description:
      "This is a description of project 2. It involves data science and AI.",
    technologies: ["Python", "AWS Lambda", "AWS CloudFormation"],
    codeLink: "https://github.com/Vicguin65/IBM-Identity-Center-API",
    startDate: new Date(2024, 0),
    endDate: new Date(2024, 4),
  },
  {
    title: "Terraform Automation For Data Science App",
    description:
      "Terraform Automation was a project that ran during my Summer 2024 semester. " +
      "I started the project with three other students. Terraform Automation is a tool that " +
      "automatically launches an AWS Virtual Private Cloud containing 2 public subnets, " +
      "2 private subnets, with 4 total t2.large Ubuntu servers. " +
      "These servers host a data science application about the accuracy of polygraph tests. " +
      "This project automated the deployment of changes to the application.",
    technologies: ["HCP Terraform CDK", "AWS VPC", "React"],
    codeLink: "https://github.com/Vicguin65/IBM-Terraform-Automation",
    startDate: new Date(2024, 4),
    endDate: new Date(2024, 7),
  },
  {
    title: "Grouping API for Camp Students",
    description:
      "Using REST API standards and Django framework, I wrote APIs to model groups of students based on surveys in a PostgresSQL database. " +
      "Based on answers, a grouping algorithm groups the students with the most similarity. Analyzed the data of about 300 students in 2023. ",
    technologies: ["Python", "Django", "PostgreSQL"],
    startDate: new Date(2023, 0),
    endDate: new Date(2023, 3),
  },
  {
    title: "Hiring Management System Automation",
    description:
      "Using hiring management system Lever’s API, parts of hiring flow was automated. Over 100 hours are saved for each hiring season. " +
      "Trained an AI model using scikit-learn to evaluate resumes for potential hires. Model used over 1,700 past candidate data and reviewed over 300 resume during its first six months with 88% accuracy. " +
      "Hosted model on an S3 AWS server.",
    technologies: ["Python", "Scikit-Learn", "AWS S3"],
    startDate: new Date(2022, 4),
    endDate: new Date(2022, 7),
  },
  {
    title: "School Contacts Webscrape",
    description:
      "Developed application to collect school contact information using school websites through webscraping. " +
      "Over 68,000 school faculty members’ information was collected using tools such as BeautifulSoup4, Selenium, and OpenAI gpt-3.5-turbo API.",
    technologies: ["Python", "BeautifulSoup4", "Selenium", "GPT-3.5-turbo"],
    startDate: new Date(2023, 5),
    endDate: new Date(2023, 6),
  },
];

const diff_text = (dt2, dt1) => {
  // Calculate the difference in milliseconds between the two dates
  var diff_ms = Math.abs(dt2.getTime() - dt1.getTime()) / 1000;

  var diff_days = diff_ms / (60 * 60 * 24);
  var diff_months = 0;
  var diff_years = 0; 
  if(diff_days > 30){
    diff_months = diff_days/30;
    diff_days %= 30;
  }

  if(diff_months > 12){
    diff_years = diff_months / 12;
    diff_months %= 12;
  }

  var diff_text = "";
  diff_years = Math.round(diff_years);
  diff_months = Math.round(diff_months);
  diff_days = Math.round(diff_days);
  
  if(diff_years > 0){
    diff_text += diff_years + " years, ";
  }

  if(diff_months > 0){
    diff_text += diff_months + " months, ";
  }

  if(diff_days > 0){
    diff_text += diff_days + " days"
  }

  // Calculate the approximate number of years by dividing the difference in days by the average number of days in a year (365.25)
  return diff_text;
}

const date_string = (dt) =>{
  const date = dt.getDate();
  const month = dt.getMonth();
  const year = dt.getFullYear();
  const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];

  var date_str = "";
  date_str += months[month] + " " + date + ", " + year;
  return date_str
}

const same_date = (date1, date2) => {
  return (
    date1.getFullYear() === date2.getFullYear() &&
    date1.getMonth() === date2.getMonth() &&
    date1.getDate() === date2.getDate()
  );
}

exports.projects = projects;
exports.diff_text = diff_text;
exports.date_string = date_string;
exports.same_date = same_date;
