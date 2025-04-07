import React, { useState } from 'react';
import './Header.css';
import { Link } from "react-router-dom";
const Header = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <header className="header">
      <div className="header-container">
        <div className="logo">Educap</div>

        <div className={`nav-links ${isOpen ? 'open' : ''}`}>
        <Link to="/">
          Features
          </Link> 
          <Link to="/">
          About
          </Link>
          <Link to="/">
          Contact Us
          </Link>
        </div>

        <div className="menu-icon" onClick={toggleMenu}>
          <div className="bar"></div>
          <div className="bar"></div>
          <div className="bar"></div>
        </div>
      </div>
    </header>
  );
};

export default Header;