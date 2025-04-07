import { useState } from 'react';
import './FrontPage.css';

function FrontPage() {
  const [showModal, setShowModal] = useState(false);
  const [mode, setMode] = useState(null); // 'login' or 'signup'

  const openModal = () => setShowModal(true);
  const closeModal = () => {
    setShowModal(false);
    setMode(null);
  };

  return (
    <>
      <header className="header">
        <div className="logo">EduCap</div>
        <nav className="nav-links">
          <a href="#features" className="feature">Features</a>
          <a href="#about" className="about">About</a>
          

          
          <a href="#contact" className="contact">Contact Us</a>
        </nav>
      </header>

      <div className="main">
        <div className="overlay">
          <h1 >Empower your learning journey with EduCap's powerful tools and features.</h1>
          
          <div className="buttons">
            <button className="btn primary" onClick={openModal}>Get Started</button>
            
          </div>
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="modal-backdrop" onClick={closeModal}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            {!mode && (
              <>
                <h2>Welcome to EduCap</h2>
                <div className="modal-buttons">
                  <button onClick={() => setMode('login')}>Login</button>
                  <button onClick={() => setMode('signup')}>Sign Up</button>
                </div>
              </>
            )}

            {mode === 'login' && (
              <form className="form">
                <h3 className='login'>Login</h3>
                <input type="text" placeholder="Username" required />
                <input type="password" placeholder="Password" required />
                <button type="submit">Login</button>
              </form>
            )}

            {mode === 'signup' && (
              <form className="form">
                <h3>Create Account</h3>
                <input type="text" placeholder="New Username" required />
                <input type="password" placeholder="New Password" required />
                <button type="submit">Sign Up</button>
              </form>
            )}

            <button className="close-btn" onClick={closeModal}>✕</button>
          </div>
        </div>
      )}

      <div className='about1'>

      </div>
    </>
  );
}

export default FrontPage;


