import React from "react";
import { FaLinkedinIn } from "react-icons/fa";
import { MdEmail } from "react-icons/md";
import "./Footer.css";

const Footer = () => {
  return (
    <div className="footer-container">
      <div className="footer-icons">
        <a
          href="https://www.linkedin.com/in/tyler-du-link/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <FaLinkedinIn />
        </a>
        <a href="mailto:tyleryeedu@gmail.com">
          <MdEmail />
        </a>
      </div>
      <p>© Tyler Du 2025</p>
    </div>
  );
};

export default Footer;
