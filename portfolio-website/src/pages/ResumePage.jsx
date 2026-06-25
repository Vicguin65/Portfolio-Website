import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import styles from './ResumePage.module.css';

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  'pdfjs-dist/build/pdf.worker.min.mjs',
  import.meta.url,
).toString();

function ResumePage() {
  const [zoomed, setZoomed] = useState(false);

  return (
    <div className="page-wrapper">
      <NavBar />
      <main className={styles.main}>

        <div className={`container ${styles.header}`}>
          <div>
            <span className="section-label">Resume</span>
            <h1 className={styles.title}>Tyler Du</h1>
          </div>
          <a
            href="https://whoistylerdu.com/Resume_Tyler_Du.pdf"
            download="Resume_Tyler_Du.pdf"
            className="btn-primary"
          >
            Download PDF ↓
          </a>
        </div>

        <div className={styles.pdfWrapper}>
          <div
            className={`${styles.pdfContainer} ${zoomed ? styles.zoomed : ''}`}
            onClick={() => setZoomed(z => !z)}
            style={{ cursor: zoomed ? 'zoom-out' : 'zoom-in' }}
            title={zoomed ? 'Click to zoom out' : 'Click to zoom in'}
          >
            <Document file="https://whoistylerdu.com/Resume_Tyler_Du.pdf">
              <Page
                pageNumber={1}
                renderTextLayer={false}
                renderAnnotationLayer={false}
              />
            </Document>
          </div>
        </div>

      </main>
      <Footer />
    </div>
  );
}

export default ResumePage;
