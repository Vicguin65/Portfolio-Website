// App.js
import React from "react";
import { Parallax, ParallaxLayer } from "@react-spring/parallax";
import { Link } from "react-router-dom";
import thoughtBubble from "./assets/thoughtbubble.png"; // Thought bubble image
import "./App.css";

function App() {
  return (
    <Parallax pages={4} style={{ backgroundColor: "#090904" }}>
      {/* Background layer */}
      <ParallaxLayer offset={0} speed={1} className="background-layer">
        <h1 className="title">Welcome to Tyler's World</h1>
      </ParallaxLayer>

      {/* Question Layer 1 */}
      <ParallaxLayer
        offset={0.7}
        speed={0.8}
        factor={1.1}
        className="background-layer question-layer cloud"
      >
        <h2 className="question-text">Who is Tyler?</h2>
      </ParallaxLayer>

      {/* Question Layer 2 */}
      <ParallaxLayer
        offset={1.3}
        speed={0.7}
        factor={1.1}
        className="background-layer question-layer cloud"
      >
        <h2 className="question-text">What does Tyler develop?</h2>
      </ParallaxLayer>

      {/* Question Layer 3 */}
      <ParallaxLayer
        offset={2}
        speed={0.6}
        factor={1.1}
        className="background-layer question-layer cloud"
      >
        <h2 className="question-text">What does Tyler enjoy doing?</h2>
      </ParallaxLayer>

      <ParallaxLayer
        offset={3}
        speed={0}
        className="background-layer question-layer"
      >
        <Link to={`/home`} className="bottom-button button-link">
          Click here to find out!
        </Link>
      </ParallaxLayer>
    </Parallax>
  );
}

export default App;
