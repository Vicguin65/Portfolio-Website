import { Parallax, ParallaxLayer } from "@react-spring/parallax";
import tyler from "./assets/tyler-removebg-preview.png";
import thought from "./assets/thoughtbubble.png";
import land from "./assets/landbetter.jpg";
import moon from "./assets/moon.jpg";
import thinking from "./assets/thinking.png"
import idea from "./assets/idea.png"
import { Link } from "react-router-dom";

import {BrowserRouter as Router, Route} from 'react-router-dom';

import "./App.css";

function App() {
  return (
    <Parallax pages={5}>
      <ParallaxLayer
        offset={0}
        speed={1}
        factor={2.1}
        style={{
          backgroundImage: `url(${moon})`,
          backgroundSize: "cover",
        }}
      ></ParallaxLayer>
      <ParallaxLayer
        offset={3}
        speed={1}
        factor={3}
        style={{
          backgroundImage: `url(${land})`,
          backgroundSize: "cover",
        }}
      ></ParallaxLayer>
      <ParallaxLayer
        className="linear-gradient"
        offset={1}
        factor={4.1}
        speed={1}
      ></ParallaxLayer>
      <ParallaxLayer className="cloud" 
        offset={0.35}
        speed={0.1}
        >
        <img src={thought} className="img-fluid image" alt="..."></img>
        <h1 className="text">Who is Tyler Du?</h1>
      </ParallaxLayer>
      <ParallaxLayer sticky={{ start: 0.5, end: 1.9 }} className="thinking" 
       offset={0.6}
       >
        <img src={thinking} alt="..." />
      </ParallaxLayer>
      <ParallaxLayer
        offset={4}
        speed={1.2}
        className="tyler-happy"
      >
        <img src={tyler} alt="tyler_happy" />
      </ParallaxLayer>
      <ParallaxLayer
      offset={4}
      speed={1.1}
      className="lightbulb"
      >
        <img src={idea} alt="lightbulb"/>
      </ParallaxLayer>
      <ParallaxLayer
      offset={4.4}
      speed={1.5}
      >
        <div className="text-center">
          <Link to={`home`} className="btn btn-success btn-lg">Click here to find out!</Link>
        </div>
      </ParallaxLayer>
    </Parallax>
  );
}

export default App;
