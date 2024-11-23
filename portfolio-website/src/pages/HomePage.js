import React from "react";
import { Link } from "react-router-dom";
import NavBar from "../components/NavBar";
import "./HomePage.css";

function HomePage() {
  return (
    <div>
      <NavBar />
      <section className="container">
        <h1>Well... Who is Tyler?</h1>
        <p>
          Hey there! I’m Tyler – a curious developer, computer science
          enthusiast, and problem-solver. From coding up web apps to diving into
          open-source, I love creating and solving problems with code. Take a
          look around to see my journey, projects, and what keeps me excited
          about tech. Let’s connect and maybe even collaborate on something
          cool!
        </p>
        <div className="link-container">
          <Link to="/resume" className="bottom-button">
            View My Resume
          </Link>
          <Link to="/projects" className="bottom-button">
            Explore My Projects
          </Link>
        </div>
      </section>
    </div>
  );
}

export default HomePage;
