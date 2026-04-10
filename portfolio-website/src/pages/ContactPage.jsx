import React, { useState } from 'react';
import { FaLinkedinIn, FaGithub } from 'react-icons/fa';
import { MdEmail } from 'react-icons/md';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import styles from './ContactPage.module.css';

const ContactPage = () => {
  const [form,      setForm]      = useState({ name: '', email: '', message: '' });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = e =>
    setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));

  const handleSubmit = e => {
    e.preventDefault();
    // TODO Phase 2: POST to FastAPI backend
    setSubmitted(true);
  };

  return (
    <div className="page-wrapper">
      <NavBar />
      <main className={`container ${styles.main}`}>

        <div className={styles.header}>
          <span className="section-label">Contact</span>
          <h1 className={styles.title}>Let's connect</h1>
          <p className={styles.subtitle}>
            Curious about my work, thinking about collaborating, or just want to chat?
            I'm all ears — reach out any time.
          </p>
        </div>

        <div className={styles.layout}>

          {/* ── Info column ── */}
          <div className={styles.infoCol}>
            <h2 className={styles.infoHeading}>Reach out</h2>
            <div className={styles.contactLinks}>
              <a href="mailto:tyleryeedu@gmail.com" className={styles.contactLink}>
                <MdEmail className={styles.contactIcon} />
                <span>tyleryeedu@gmail.com</span>
              </a>
              <a
                href="https://www.linkedin.com/in/tyler-du-link/"
                target="_blank"
                rel="noopener noreferrer"
                className={styles.contactLink}
              >
                <FaLinkedinIn className={styles.contactIcon} />
                <span>LinkedIn</span>
              </a>
              <a
                href="https://github.com/Vicguin65"
                target="_blank"
                rel="noopener noreferrer"
                className={styles.contactLink}
              >
                <FaGithub className={styles.contactIcon} />
                <span>GitHub</span>
              </a>
            </div>
          </div>

          {/* ── Form column ── */}
          <div className={styles.formCol}>
            {submitted ? (
              <div className={styles.success}>
                <h3 className={styles.successTitle}>Message sent!</h3>
                <p>Thanks for reaching out — I'll get back to you soon.</p>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className={styles.form}>
                <div className={styles.field}>
                  <label className={styles.label}>Name</label>
                  <input
                    type="text"
                    name="name"
                    value={form.name}
                    onChange={handleChange}
                    placeholder="Your name"
                    required
                    className={styles.input}
                  />
                </div>
                <div className={styles.field}>
                  <label className={styles.label}>Email</label>
                  <input
                    type="email"
                    name="email"
                    value={form.email}
                    onChange={handleChange}
                    placeholder="you@example.com"
                    required
                    className={styles.input}
                  />
                </div>
                <div className={styles.field}>
                  <label className={styles.label}>Message</label>
                  <textarea
                    name="message"
                    value={form.message}
                    onChange={handleChange}
                    placeholder="What's on your mind?"
                    rows={5}
                    required
                    className={styles.textarea}
                  />
                </div>
                <button type="submit" className={`btn-primary ${styles.submitBtn}`}>
                  Send message →
                </button>
              </form>
            )}
          </div>

        </div>
      </main>
      <Footer />
    </div>
  );
};

export default ContactPage;
