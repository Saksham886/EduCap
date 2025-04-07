import './FeaturePage.css';


function FeaturePage() {
  return (
    <>
    <div className="features-page" id="features">
      <h1 className="page-title">Features</h1>
      <div className="card-container">
        {/* <div className="feature-card">
          <div className="card-header">
            <h2>Speech to Text</h2>
          </div>
          <p>
            Convert your spoken words into written text instantly.
            Designed for users with limited mobility or visual challenges, this feature makes typing effortless and communication more inclusive. Just speak — we’ll do the writing for you.
          </p>
          <button className="stt">Try Me</button>
        </div> */}

        <div className="feature-card">
          <div className="card-header">
            <h2>Text to Speech</h2>
          </div>
          <p>
            This feature reads text aloud to assist users with visual impairments or reading difficulties. Hear your content come to life.
          </p>
          <button className="stt">Try Me</button>
        </div>

        <div className="feature-card">
          <div className="card-header">
            <h2>Summarizer</h2>
          </div>
          <p>
            Get quick summaries of long text. Perfect for users with cognitive disabilities or limited attention span who need essential points fast.
          </p>
          <button className="stt">Try Me</button>
        </div>

        <div className="feature-card">
          <div className="card-header">
            <h2>AI Bot</h2>
          </div>
          <p>
            Ask anything, anytime. Our intelligent assistant supports students by answering questions and giving guidance in an inclusive way.
          </p>
          <button className="stt">Try Me</button>
        </div>
      </div>
    </div>
    <div className="about1" id="about">
  <div className="about-content">
    <div className="about-text">
      <h2>About Us</h2>
      <p>
        EduCap is a powerful educational platform designed to empower learners of all abilities. 
        Whether you're facing visual, cognitive, or mobility challenges, EduCap brings together 
        smart features like speech-to-text, text-to-speech, summarization, and an intelligent AI Bot — 
        all tailored to enhance accessibility and inclusivity. Our mission is to make learning more 
        intuitive, personalized, and barrier-free for everyone.
      </p>
    </div>
    <div className="about-image">
      <img src="https://images.unsplash.com/photo-1584697964154-e82c3f76b1fa?auto=format&fit=crop&w=800&q=60" alt="About EduCap" />
    </div>
  </div>
</div>
<div className="contact-us" id="contact">
  <h2>Contact Us</h2>
  <h3>Have questions or need assistance? We're here to help.</h3>
  <div className="contact-container">
    {/* Left Side: Contact Info */}
    <div className="contact-info">
      <p><strong>Email:</strong> support@educap.com</p>
      <p><strong>Phone:</strong> +91 9876543210</p>
      <p><strong>Address:</strong> BMS College, Bangalore,Karnataka</p>
    </div>

    {/* Right Side: Contact Form */}
    <form className="contact-form">
      <input type="text" placeholder="Your Name" required />
      <input type="email" placeholder="Your Email" required />
      <input type="text" placeholder="Subject" required />
      <textarea placeholder="Message" rows="5" required></textarea>
      <button type="submit">Submit</button>
    </form>
  </div>
</div>

<footer className="footer">
  <div className="footer-content">
    <div className="footer-left">
      <h3>EduCap</h3>
      <p>Empowering every learner, everywhere.</p>
    </div>
    <div className="footer-right">
      <p><strong>Email:</strong> support@educap.com</p>
      <p><strong>Phone:</strong> +91 9876543210</p>
      <p><strong>© {new Date().getFullYear()} EduCap. All rights reserved.</strong></p>
    </div>
  </div>
</footer>

    </>
    
  );
}

export default FeaturePage;

