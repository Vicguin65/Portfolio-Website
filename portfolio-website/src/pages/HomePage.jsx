import React from 'react';
import { Link } from 'react-router-dom';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import './HomePage.css';

const skills = [
  'Python', 'React', 'JavaScript', 'TypeScript', 'AWS',
  'Django', 'FastAPI', 'PostgreSQL', 'Docker', 'Terraform',
  'Git', 'Linux',
];

function HomePage() {
  return (
    <div className="page-wrapper">
      <NavBar />
      <main>

        {/* ── About ── */}
        <section className="about-section container">
          <div className="about-text">
            <span className="section-label">About me</span>
            <h1 className="about-heading">
              Who is <em className="about-name">Tyler Du</em>?
            </h1>
            <p className="about-bio">
              Who is Tyler Du? Well, I am a computer science graduate from RPI with a passion
              for building things end-to-end, from web apps and cloud infrastructure to
              open-source projects and AI-powered tools. I'm driven by the question <strong>"what if?"</strong> and
              thrive at the intersection of software engineering and creative problem-solving.
              Take a look around to see my journey, projects, and what keeps me excited about tech.
            </p>
            <div className="about-actions">
              <Link to="/resume"   className="btn-primary">View Resume</Link>
              <Link to="/projects" className="btn-secondary">My Projects →</Link>
            </div>
          </div>

          <div className="about-photo-col">
            <div className="about-photo-frame">
              <img
                src="https://whoistylerdu.com/tyler.jpg"
                alt="Tyler Du"
                className="about-photo"
              />
            </div>
          </div>
        </section>

        {/* ── Skills ── */}
        <section className="skills-section container">
          <span className="section-label">Tech stack</span>
          <h2 className="skills-heading">What I work with</h2>
          <div className="skills-grid">
            {skills.map(skill => (
              <span key={skill} className="skill-chip">{skill}</span>
            ))}
          </div>
        </section>

      </main>
      <Footer />
    </div>
  );
}

export default HomePage;
