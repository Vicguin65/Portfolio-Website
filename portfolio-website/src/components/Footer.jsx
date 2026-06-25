import React from 'react';
import { FaLinkedinIn, FaGithub } from 'react-icons/fa';
import { MdEmail } from 'react-icons/md';
import './Footer.css';

const Footer = () => (
  <footer className="footer">
    <div className="footer-inner container">
      <span className="footer-brand">Tyler Du</span>
      <div className="footer-links">
        <a
          href="https://www.linkedin.com/in/tyler-du-link/"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="LinkedIn"
        >
          <FaLinkedinIn />
        </a>
        <a
          href="https://github.com/Vicguin65"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="GitHub"
        >
          <FaGithub />
        </a>
        <a href="mailto:tyleryeedu@gmail.com" aria-label="Email">
          <MdEmail />
        </a>
      </div>
      <p className="footer-copy">© {new Date().getFullYear()} Tyler Du</p>
    </div>
  </footer>
);

export default Footer;
