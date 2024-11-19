import React from "react";
import "./ProjectPage.css";
import NavBar from "../components/NavBar";

const { projects, diff_text, date_string, same_date } = require("../components/projects");

const ProjectPage = () => {
  return (
    <div>
      <NavBar></NavBar>

      <div className="container">
        <h1 className="header">What are Tyler's Projects?</h1>
        <div className="projectsContainer">
          {projects
            .sort(function (a, b) {
              return b.endDate.getTime() - a.endDate.getTime();
            })
            .map((project, index) => (
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
                <h5>{"Project Start Date: " + date_string(project.startDate)}</h5>
                <h5>{same_date(new Date(), project.endDate) ? "Project is actively being worked on!" : "Project End Date: " + date_string(project.endDate)}</h5>
                <h2>
                  {"Project Duration: " +
                    diff_text(project.startDate, project.endDate)}
                </h2>
              </div>
            ))}
        </div>
      </div>
    </div>
  );
};

export default ProjectPage;
