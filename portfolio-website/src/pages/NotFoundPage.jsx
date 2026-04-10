import React from 'react';
import { Link } from 'react-router-dom';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import './NotFoundPage.css';

const NotFoundPage = () => (
  <div className="page-wrapper">
    <NavBar />
    <main className="not-found">
      <span className="section-label">404</span>
      <h1 className="not-found-title">Page not found</h1>
      <p className="not-found-sub">
        Hmm, that page seems to have drifted away into the clouds.
      </p>
      <Link to="/home" className="btn-primary">Back home →</Link>
    </main>
    <Footer />
  </div>
);

export default NotFoundPage;
