import { Parallax, ParallaxLayer } from "@react-spring/parallax";
import tyler from "./assets/tyler-removebg-preview.png";
import thought from "./assets/thoughtbubble.png";
import land from "./assets/landbetter.jpg";
import moon from "./assets/moon.jpg";
import "./App.css";

function App() {
  return (
    <Parallax pages={5}>
      <style>background-image: linear-gradient(red, yellow)</style>
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
      <ParallaxLayer sticky={{ start: 0.3, end: 3.4 }} className="cloud">
        <img src={thought} className="img-fluid" alt="..." />
      </ParallaxLayer>
    </Parallax>
  );
}

export default App;
