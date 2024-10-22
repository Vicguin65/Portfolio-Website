import React from "react";
import { Link } from "react-router-dom";

function HomePage() {
  return (
    <div>
      <section>
        <h5>Well... Who is Tyler?</h5>
        <text>
          Hey there! I’m Tyler – a curious developer, computer science
          enthusiast, and problem-solver. From coding up web apps to diving into
          open-source, I love creating and solving problems with code. Take a
          look around to see my journey, projects, and what keeps me excited
          about tech. Let’s connect and maybe even collaborate on something
          cool!
        </text>
      </section>
      <div>
        <Link to={`/resume`}>Click here to view my resume</Link>
      </div>

      <Link to={`/projects`}>Click here to see projects</Link>
    </div>
  );
}

export default HomePage;
