import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './App.css';

function App() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const id = setTimeout(() => setVisible(true), 80);
    return () => clearTimeout(id);
  }, []);

  return (
    <div className="landing">
      {/* Floating dream blobs */}
      <div className="blob blob-1" aria-hidden="true" />
      <div className="blob blob-2" aria-hidden="true" />
      <div className="blob blob-3" aria-hidden="true" />

      <div className={`hero ${visible ? 'hero--visible' : ''}`}>
        <span className="hero-pill">Software Engineer</span>
        <h1 className="hero-heading">
          Hello, I'm <em>Tyler Du</em>
        </h1>
        <p className="hero-sub">
          I build thoughtful software and love asking&nbsp;<strong>"what if?"</strong>
        </p>
        <Link to="/home" className="hero-cta">
          Explore my work <span aria-hidden="true">→</span>
        </Link>
      </div>

      <div className="scroll-hint" aria-hidden="true">
        <div className="scroll-line" />
      </div>
    </div>
  );
}

export default App;
