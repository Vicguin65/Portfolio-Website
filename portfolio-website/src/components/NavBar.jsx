import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './NavBar.css';

const links = [
  { to: '/home',     label: 'Home' },
  { to: '/projects', label: 'Projects' },
  { to: '/resume',   label: 'Resume' },
  { to: '/contact',  label: 'Contact' },
  { to: '/ask',      label: 'Ask Tyler' },
];

const NavBar = () => {
  const [scrolled,  setScrolled]  = useState(false);
  const [menuOpen,  setMenuOpen]  = useState(false);
  const location = useLocation();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  // Close mobile menu on route change
  useEffect(() => { setMenuOpen(false); }, [location.pathname]);

  return (
    <nav className={`navbar ${scrolled ? 'navbar--scrolled' : ''}`}>
      <Link to="/home" className="navbar-brand">Tyler Du</Link>

      <button
        className={`navbar-toggle ${menuOpen ? 'navbar-toggle--open' : ''}`}
        onClick={() => setMenuOpen(o => !o)}
        aria-label="Toggle navigation"
        aria-expanded={menuOpen}
      >
        <span /><span /><span />
      </button>

      <ul className={`navbar-links ${menuOpen ? 'navbar-links--open' : ''}`}>
        {links.map(({ to, label }) => (
          <li key={to}>
            <Link
              to={to}
              className={`navbar-link ${location.pathname === to ? 'navbar-link--active' : ''}`}
            >
              {label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default NavBar;
