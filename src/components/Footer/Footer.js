import React from 'react'
import './footer.css'
import { Link } from "react-router-dom";
import {HashLink} from "react-router-hash-link";

const Footer = () => {
    return (
        <footer>
            <h1><HashLink to="/#top">OPTplan</HashLink></h1>
            <div className="footer-links">
                <h2><HashLink to="/#top">Home</HashLink></h2>
                <h2><HashLink to="/generate/#top">Generate</HashLink></h2>
                <h2><HashLink to="/verify/#top">Verify</HashLink></h2>
            </div>
            <p>© 2024 Impana Chimmalagi, All rights reserved.</p>
        </footer>
    )
}

export default Footer