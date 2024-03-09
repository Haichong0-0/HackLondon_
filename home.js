import React from 'react'

import projectStyles from '.style.module.css'
import styles from './home.module.css'

const Home = (props) => {
  return (
    <div className={styles['container']}>
      <div className={styles['container1']}>
        <div className={styles['container2']}>
          <div className={styles['container3']}>
            <span className={styles['text']}>
              <span>Project</span>
              <br></br>
            </span>
            <span className={styles['des']}>This project is about</span>
          </div>
          <div className={styles['container4']}>
            <form className={styles['form']}>
              <textarea
                placeholder="placeholder"
                className={` ${styles['textarea']} ${projectStyles['textarea']} `}
              ></textarea>
              <button
                type="button"
                className={` ${styles['button']} ${projectStyles['button']} `}
              >
                UPDATE
              </button>
            </form>
          </div>
        </div>
        <div className={styles['container5']}>
          <button
            type="button"
            className={` ${styles['button1']} ${projectStyles['button']} `}
          >
            IMPORT TO CALENDER
          </button>
        </div>
      </div>
    </div>
  )
}

export default Home
