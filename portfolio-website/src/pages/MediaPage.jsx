import React from 'react';
import { Link } from 'react-router-dom';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import { media } from '../components/media';
import './MediaPage.css';

const MONTHS = [
  'January','February','March','April','May','June',
  'July','August','September','October','November','December',
];

const date_string = (dt) =>
  `${MONTHS[dt.getMonth()]} ${dt.getDate()}, ${dt.getFullYear()}`;

const MediaPage = () => {
  const sorted = [...media].sort((a, b) => b.date - a.date);

  return (
    <div className="page-wrapper">
      <NavBar />
      <main>

        <section className="media-header container">
          <span className="section-label">Press &amp; Features</span>
          <h1 className="media-title">In the News</h1>
          <p className="media-subtitle">
            A collection of times my work has been recognized by publications,
            organizations, and the broader community.
          </p>
        </section>

        <section className="media-list-section container">
          <div className="media-list">
            {sorted.map((item) => (
              <article key={item.slug} className="media-card">
                <div className="media-card-meta">
                  <span className="media-publication">{item.publication}</span>
                  <span className="media-date">{date_string(item.date)}</span>
                </div>

                <h2 className="media-card-title">
                  <Link to={`/features/${item.slug}`} className="media-card-title-link">
                    {item.title}
                  </Link>
                </h2>

                <p className="media-card-description">{item.description}</p>

                <div className="media-card-footer">
                  <div className="media-tags">
                    {item.tags.map((tag) => (
                      <span key={tag} className="media-tag">{tag}</span>
                    ))}
                  </div>
                  <Link to={`/features/${item.slug}`} className="media-read-more">
                    View feature ↗
                  </Link>
                </div>
              </article>
            ))}
          </div>
        </section>

      </main>
      <Footer />
    </div>
  );
};

export default MediaPage;
