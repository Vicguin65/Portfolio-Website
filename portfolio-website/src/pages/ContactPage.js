import React from "react";
import NavBar from "../components/NavBar";
import styles from "./ContactPage.module.css";

const ContactPage = () => {
  return (
    <div>
      <NavBar />
      <h1 className={styles.header}>Contact Me</h1>
      <h2>CURRENTLY IN DEVELOPMENT</h2>
      {/* TO DO: Connect with backend */}
      <div>
        <h3>Got Questions? Me Too.</h3>
        <p>
          Curiosity sparks connection. Whether you're wondering about my work,
          thinking about collaborating, or just want to chat, I'm all ears. Ask
          away—I’d love to talk. Reach out via the form below or email me at{" "}
          <a href="mailto:tyleryeedu@gmail.com">tyleryeedu@gmail.com</a>.
        </p>
        <h4>Follow me</h4>
        <a href="https://www.linkedin.com/in/tyler-du-link/">LinkedIn</a>
      </div>
      <form onSubmit={() => {}}>
        <div>
          <input type="text" placeholder="Your name" name="name" required />
        </div>
        <div>
          <input type="email" placeholder="Email" name="email" required />
        </div>
        <div>
          <textarea
            placeholder="Enter your message here."
            name="message"
            required
          />
        </div>
        <div>
          <button type="submit"> Send a message </button>
        </div>
      </form>
    </div>
  );
};

export default ContactPage;
