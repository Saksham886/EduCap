import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
        <div className="footer-content">
          <div className="footer-left">
            <h3>EduCap</h3>
            <p>Empowering every learner, everywhere.</p>
          </div>
          <div className="footer-right">
            <p><strong>Email:</strong> support@educap.com</p>
            {/* <p><strong>Phone:</strong> +91 9876543210</p> */}
            <p><strong>© {new Date().getFullYear()} EduCap. All rights reserved.</strong></p>
          </div>
        </div>
      </footer>
  );
};

export default Footer;