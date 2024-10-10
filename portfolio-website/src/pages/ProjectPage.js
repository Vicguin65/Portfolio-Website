import React from "react";
import "./ProjectPage.css"; // Importing the external CSS file

// Sample data for projects
const projects = [
  {
    title: "Accessible Routes",
    description:
      "Accessible Routes was a website that was worked on during Fall 2023 and Spring 2024. Using RPI's accessibility data, I created a backend API that provided the accessible routes between buildings on campus.",
    technologies: ["React", "Django", "CSS", "AWS EC2"],
    link: "https://github.com/Accessible-Routes",
  },
  {
    title: "REST API For AWS Identity Store",
    description:
      "This is a description of project 2. It involves data science and AI.",
    technologies: ["Python", "AWS Lambda", "AWS CloudFormation"],
    // No link provided for this project
  },
  
];

const ProjectPage = () => {
  return (
    <div className="container">
      <h1 className="header">What are Tyler's Projects?</h1>
      <div className="projectsContainer">
        {projects.map((project, index) => (
          <div key={index} className="projectCard">
            <h2>{"What is " + project.title + "?"}</h2>
            <p>{project.description}</p>
            <div className="techContainer">
              {project.technologies.map((tech, i) => (
                <span key={i} className="techBadge">
                  {tech}
                </span>
              ))}
            </div>
            {/* Conditionally rendering the link if it exists */}
            {project.link ? (
              <a
                href={project.link}
                target="_blank"
                rel="noopener noreferrer"
                className="projectLink"
              >
                View Project
              </a>
            ) : null}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProjectPage;
