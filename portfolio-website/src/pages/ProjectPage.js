import React from "react";
import "./ProjectPage.css"; // Importing the external CSS file

const {projects} = require("../components/projects")


const ProjectPage = () => {
  return (
    <div className="container">
      <h1 className="header">What are Tyler's Projects?</h1>
      <div className="projectsContainer">
        {projects.sort(function(a,b){
          return b.endDate.getTime() - a.endDate.getTime()
        }).map((project, index) => (
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
            {project.codeLink ? (
              <a
                href={project.codeLink}
                target="_blank"
                rel="noopener noreferrer"
                className="projectLink"
              >
                View Project
              </a>
            ) : null}
            {/* TODO: change how this is visualized */}
            {project.endDate.getTime()}
            {/* {project.endDate.toString()} */}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProjectPage;
