import React from 'react';
import { useParams, Link, Navigate } from 'react-router-dom';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import { media } from '../components/media';
import styles from './MediaDetailPage.module.css';

const MONTHS = [
  'January','February','March','April','May','June',
  'July','August','September','October','November','December',
];

const date_string = (dt) =>
  `${MONTHS[dt.getMonth()]} ${dt.getDate()}, ${dt.getFullYear()}`;

const MediaDetailPage = () => {
  const { slug } = useParams();
  const item = media.find((m) => m.slug === slug);

  if (!item) return <Navigate to="/features" replace />;

  return (
    <div className="page-wrapper">
      <NavBar />
      <main>
        <article className={`${styles.article} container`}>

          <Link to="/features" className={styles.back}>← Back to Features</Link>

          <header className={styles.header}>
            <div className={styles.meta}>
              <span className={styles.publication}>{item.publication}</span>
              <span className={styles.date}>{date_string(item.date)}</span>
            </div>
            <h1 className={styles.title}>{item.title}</h1>
            <div className={styles.tags}>
              {item.tags.map((tag) => (
                <span key={tag} className={styles.tag}>{tag}</span>
              ))}
            </div>
          </header>

          {item.description && (
            <p className={styles.description}>{item.description}</p>
          )}

          {item.images.length > 0 && (
            <div className={styles.images}>
              {item.images.map((img, i) => (
                <figure key={i} className={styles.figure}>
                  <img src={img.src} alt={img.alt} className={styles.image} />
                  {img.caption && (
                    <figcaption className={styles.caption}>{img.caption}</figcaption>
                  )}
                </figure>
              ))}
            </div>
          )}

          {item.videos.length > 0 && (
            <div className={styles.videos}>
              {item.videos.map((video, i) => (
                <div key={i} className={styles.videoWrapper}>
                  {video.type === 'youtube' ? (
                    <iframe
                      src={`https://www.youtube-nocookie.com/embed/${video.id}`}
                      title={video.title || 'Video'}
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                      className={styles.iframe}
                    />
                  ) : (
                    <video src={video.url} controls className={styles.iframe} />
                  )}
                </div>
              ))}
            </div>
          )}

          {item.links.length > 0 && (
            <div className={styles.links}>
              <h2 className={styles.linksHeading}>Source</h2>
              <div className={styles.linkList}>
                {item.links.map((link, i) => (
                  <a
                    key={i}
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={styles.externalLink}
                  >
                    {link.label} ↗
                  </a>
                ))}
              </div>
            </div>
          )}

        </article>
      </main>
      <Footer />
    </div>
  );
};

export default MediaDetailPage;
