import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import styles from './AskTylerPage.module.css';

const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

function AskTylerPage() {
  const [jd, setJd] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [fullResponse, setFullResponse] = useState('');
  const [displayed, setDisplayed] = useState('');
  const intervalRef = useRef(null);

  // Typewriter: reveal response word-by-word after it arrives
  useEffect(() => {
    if (!fullResponse) return;

    clearInterval(intervalRef.current);
    const words = fullResponse.split(' ');
    let idx = 0;
    setDisplayed('');

    intervalRef.current = setInterval(() => {
      if (idx < words.length) {
        setDisplayed(prev => (idx === 0 ? words[0] : prev + ' ' + words[idx]));
        idx++;
      } else {
        clearInterval(intervalRef.current);
      }
    }, 35);

    return () => clearInterval(intervalRef.current);
  }, [fullResponse]);

  const handleSubmit = async e => {
    e.preventDefault();
    if (!jd.trim()) return;

    setLoading(true);
    setError(false);
    setFullResponse('');
    setDisplayed('');

    try {
      const res = await fetch(`${API_URL}/api/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ job_description: jd }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setFullResponse(data.response);
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-wrapper">
      <NavBar />
      <main className={styles.main}>
        <div className="container">
          <span className="section-label">AI Assistant</span>
          <h1 className={styles.title}>Ask Tyler</h1>
          <p className={styles.subtitle}>
            Paste a job description and get an honest evaluation of Tyler's fit,
            his most relevant work, and talking points for the interview.
          </p>

          <form onSubmit={handleSubmit} className={styles.form}>
            <textarea
              className={styles.textarea}
              placeholder="Paste the job description here..."
              value={jd}
              onChange={e => setJd(e.target.value)}
              rows={12}
            />
            <button
              type="submit"
              className={`btn-primary ${styles.submit}`}
              disabled={loading || !jd.trim()}
            >
              {loading ? 'Analyzing...' : 'Evaluate Fit →'}
            </button>
          </form>

          {loading && (
            <div className={styles.thinking}>
              <span className={styles.dot} style={{ animationDelay: '0ms' }} />
              <span className={styles.dot} style={{ animationDelay: '160ms' }} />
              <span className={styles.dot} style={{ animationDelay: '320ms' }} />
            </div>
          )}

          {error && (
            <p className={styles.error}>Something went wrong. Please try again.</p>
          )}

          {displayed && (
            <div className={styles.response}>
              <div className={styles.responseText}>
                <ReactMarkdown>{displayed}</ReactMarkdown>
              </div>
            </div>
          )}
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default AskTylerPage;
