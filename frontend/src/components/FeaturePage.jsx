import './FeaturePage.css';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';


function FeaturePage() {
  useEffect(() => {
    const elements = document.querySelectorAll('.fade-in-up');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animation = 'fadeInUp 1s ease-out forwards';
        }
      });
    }, { threshold: 0.1 });

    elements.forEach(el => observer.observe(el));
    return () => elements.forEach(el => observer.unobserve(el));
  }, []);

  const handleChatOpen = () => {
    alert("Launching AI Chat Bot (coming soon!)");
  };
  const navigate = useNavigate();

const goToSummarizer = () => {
  navigate('/summarizer');
};


  return (
    <>
      <div className="features-page" id="features">
        <h1 className="page-title">Features</h1>
        <div className="card-container">
          <div className="feature-card fade-in-up">
            <div className="card-front">
              <div className="card-header">
                <h2>Text to Speech</h2>
              </div>
              <p>
                This feature reads text aloud to assist users with visual impairments or reading difficulties.
              </p>
              <button className="stt">Try Me</button>
            </div>
            <div className="card-back">
              <p>Supported in multiple languages. Great for visually impaired users.</p>
            </div>
          </div>

          <div className="feature-card fade-in-up">
            <div className="card-front">
              <div className="card-header">
                <h2>Summarizer</h2>
              </div>
              <p>
                Get quick summaries of long text. Perfect for users with cognitive disabilities or short attention spans.
              </p>
              <button className="stt">Try Me</button>
            </div>
            <div className="card-back">
              <p>Uses AI to extract key points instantly and clearly.</p>
            </div>
          </div>

          <div className="feature-card fade-in-up">
            <div className="card-front">
              <div className="card-header">
                <h2>AI Bot</h2>
              </div>
              <p>
                Ask anything, anytime. Our assistant supports students by answering questions and giving guidance.
              </p>
              <button className="stt">Try Me</button>
            </div>
            <div className="card-back">
              <p>Available 24/7 for doubt clearing, homework help, and more.</p>
            </div>
          </div>
        </div>
      </div>

      <div className="about1" id="about">
        <div className="about-content fade-in-up">
          <div className="about-text">
            <h2>About Us</h2>
            <p>
            Welcome to Educap – where education meets accessibility. At Educap, our mission is to make learning inclusive, personalized, and empowering for every student. We are building an AI-driven learning assistant designed to support students with visual, hearing, and cognitive disabilities, ensuring that no one is left behind in their educational journey.
            Using the power of artificial intelligence and assistive technology, Educap adapts to each learner’s unique needs—offering features like text-to-speech, sign language support, cognitive-friendly content, and intuitive learning paths. Our platform creates a supportive digital environment that helps students learn confidently, comfortably, and independently.
            We’re not just building a tool—we’re building a movement for accessible education. At Educap, we believe that learning should be limitless, and we're committed to making that a reality for everyone.
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
        <div className="contact-container fade-in-up">
          <div className="contact-info">
            <p><strong>Email:</strong> support@educap.com</p>
            <p><strong>Phone:</strong> +91 9876543210</p>
            <p><strong>Address:</strong> BMS College, Bangalore, Karnataka</p>
          </div>

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

      <div className="chat-btn" onClick={handleChatOpen}>
        💬
      </div>
    </>
  );
}

export default FeaturePage;


