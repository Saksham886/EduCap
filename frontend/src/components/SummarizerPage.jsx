import React from 'react';
import './SummarizerPage.css'; // Optional: external CSS

const SummarizerPage = () => {
  return (
    <div className="summarizer-page">
      <h1 className="main-heading">Summarizer</h1>
      <div className="summary-options">
        <div className="option">
          <h2>Summarize from YouTube</h2>
          <p>Paste a YouTube link to get a summary of the video content.</p>
        </div>
        <div className="option">
          <h2>Summarize from PDF</h2>
          <p>Upload a PDF file and get a concise summary of the document.</p>
        </div>
        <div className="option">
          <h2>Summarize from Text</h2>
          <p>Enter any text or paragraph you want summarized instantly.</p>
        </div>
        <div className="option">
          <h2>Summarize from News Article</h2>
          <p>Provide a news link and receive a short summary of the article.</p>
        </div>
      </div>
    </div>
  );
};

export default SummarizerPage;
