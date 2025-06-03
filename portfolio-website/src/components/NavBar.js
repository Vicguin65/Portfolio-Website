import React from "react";
import "./NavBar.css";

const NavBar = () => {
  return (
    <div className="navbar-container">
      <a href="/home">Home</a>
      <a href="/resume">Resume</a>
      <a href="/projects">Projects</a>
      <a href="/contact">Contact</a>
    </div>
  );
};

export default NavBar;
