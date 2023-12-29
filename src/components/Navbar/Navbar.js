import React from 'react';
import './navbar.css';
import { Link } from "react-router-dom";
import {HashLink} from "react-router-hash-link";
import LOGO from '../../assets/OPTplan_logo_transparent.png';

const Navbar = () => {
    return (
        <div className='navbar'>
            <div className='left'>
                <img src={LOGO}></img>
                <h1><HashLink to="/#top">OPTplan</HashLink></h1>
            </div>
            <div className='right'>
                    <h2><HashLink to="/generate/#top">Generate</HashLink></h2>
                    <h2><HashLink to="/verify/#top"> Verify </HashLink></h2>
            </div>
        </div>
    )
}

export default Navbar