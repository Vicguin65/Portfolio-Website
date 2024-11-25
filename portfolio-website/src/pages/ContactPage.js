import React from 'react'
import NavBar from '../components/NavBar'
import styles from './ContactPage.module.css'

const ContactPage = () => {
    
  return (
    <div>
        <NavBar/>
        <h1 className={styles.header}>Contact Me</h1>
        <h2>CURRENTLY IN DEVELOPMENT</h2>
        {/* TO DO: Connect with backend */}
      <form onSubmit={() => {}}>
        <div>
          <input type="text" placeholder="Your name" name="name" required />
        </div>
        <div>
          <input type="email" placeholder="Email" name="email" required />
        </div>
        <div>
          <textarea placeholder="Enter your message here." name="message" required />
        </div>
        <div>
          <button type="submit"> Send a message </button>
        </div>
      </form>
    </div>
  )
}

export default ContactPage