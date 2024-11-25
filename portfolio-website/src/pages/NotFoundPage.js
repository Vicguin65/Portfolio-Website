import React from 'react'
import NavBar from '../components/NavBar'
import styles from "./NotFoundPage.module.css"

const NotFoundPage = () => {
  return (
    <div>
        <NavBar/>
        <h1 style={styles.work}>Where is that page???</h1>
        <text>Sorry but the page you are looking for is not here.</text>
    </div>
  )
}

export default NotFoundPage