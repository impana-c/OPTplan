import React from 'react'
import './about.css'
import { Link } from "react-router-dom";
import {HashLink} from "react-router-hash-link";

const About = () => {
    return (
        <section>
          <div className="container about__container">
            <div className='flex-container-btns'>
              <button className='btn btn-primary'>
                <HashLink to="/generate/#top">
                <h1>Generate</h1>
                <h2>a new optimal plan</h2>
                </HashLink>
              </button>
              <button className='btn btn-primary'>
                <HashLink to="/verify/#top">
                <h1>Verify</h1>
                <h2>your own plan</h2>
                </HashLink>
              </button>
            </div>

            <div className='aboutText'>
            <h2 >About</h2>
            <p>Navigate the challenges of enrollment by finding the optimal class plan for your remaining years of CS undergrad at UCLA. Given the classes you have already taken, time until graduation, along with any other requests, OPTplan will generate you a schedule that meets all of your needs along with prerequisite/graduation requirements. </p>
            <p>Currently, common double majors and minors are supported. Additional support will be added for other double majors, minors, and CS-adjacent majors. More is on the way! :)</p>
            <p> <b>Note: </b> OPTplan is only built for UCLA undergraduates with Computer Science as their primary major. Any other majors are not supported at this moment. </p>
            </div>
          </div>
        </section>
    )
  }
  
  export default About