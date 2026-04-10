import React from 'react';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import { projects, diff_text, date_string, same_date } from '../components/projects';
import './ProjectPage.css';

const ProjectPage = () => {
  const sorted = [...projects].sort((a, b) => b.endDate - a.endDate);

  return (
    <div className="page-wrapper">
      <NavBar />
      <main>

        <section className="projects-header container">
          <span className="section-label">Portfolio</span>
          <h1 className="projects-title">What I've built</h1>
          <p className="projects-subtitle">
            Projects spanning cloud infrastructure, web apps, automation, and AI — each one
            started with a curious "what if?"
          </p>
        </section>

        <section className="projects-grid-section container">
          <div className="projects-grid">
            {sorted.map((project, i) => {
              const isActive = same_date(new Date(), project.endDate);
              return (
                <article key={i} className="project-card">
                  <div className="project-card-top">
                    <h2 className="project-card-title">{project.title}</h2>
                    <div className="project-dates">
                      <span>{date_string(project.startDate)}</span>
                      <span className="project-date-sep">→</span>
                      <span>{isActive ? 'Present' : date_string(project.endDate)}</span>
                    </div>
                  </div>

                  <p className="project-description">{project.description}</p>

                  <div className="project-card-footer">
                    <div className="project-tech">
                      {project.technologies.map((tech, j) => (
                        <span key={j} className="tech-badge">{tech}</span>
                      ))}
                    </div>
                    {project.codeLink && (
                      <a
                        href={project.codeLink}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="project-link"
                      >
                        View code ↗
                      </a>
                    )}
                  </div>

                  <div className="project-duration">
                    {isActive
                      ? 'Actively maintained'
                      : diff_text(project.startDate, project.endDate)}
                  </div>
                </article>
              );
            })}
          </div>
        </section>

      </main>
      <Footer />
    </div>
  );
};

export default ProjectPage;
