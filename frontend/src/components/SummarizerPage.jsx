import React, { useState } from 'react';
import './SummarizerPage.css';
import { summarizeYoutube } from '../api/summarizeYoutube';
import { summarizeText } from '../api/summarizeText';
import { summarizeArticle } from '../api/summarizeArticle';
import { summarizePdf } from '../api/summarizePdf'; // optional, explained below

const SummarizerPage = () => {
  const [activeOption, setActiveOption] = useState(null);
  const [input, setInput] = useState('');
  const [file, setFile] = useState(null);
  const [outputText, setOutputText] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    setLoading(true);
    setOutputText('');

    try {
      let response;
      switch (activeOption) {
        case 'youtube':
          response = await summarizeYoutube(input);
          break;
        case 'pdf':
          const formData = new FormData();
          formData.append('file', file);
          response = await summarizePdf(formData);
          break;
        case 'text':
          response = await summarizeText(input);
          break;
        case 'news':
          response = await summarizeArticle(input);
          break;
        default:
          response = { summary: 'Invalid selection.' };
      }
      setOutputText(response.summary);
    } catch (error) {
      console.error(error);
      setOutputText('Error summarizing. Please try again.');
    }

    setLoading(false);
  };

  const renderForm = () => {
    switch (activeOption) {
      case 'youtube':
      case 'news':
        return (
          <div className="input-area">
            <input
              type="text"
              placeholder={`Enter ${activeOption === 'youtube' ? 'YouTube URL' : 'News article URL'}`}
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={handleSummarize} disabled={loading}>
              {loading ? 'Summarizing...' : 'Summarize'}
            </button>
          </div>
        );
      case 'pdf':
        return (
          <div className="input-area">
            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setFile(e.target.files[0])}
            />
            <button onClick={handleSummarize} disabled={loading}>
              {loading ? 'Summarizing...' : 'Summarize'}
            </button>
          </div>
        );
      case 'text':
        return (
          <div className="input-area">
            <textarea
              placeholder="Paste your text here"
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={handleSummarize} disabled={loading}>
              {loading ? 'Summarizing...' : 'Summarize'}
            </button>
          </div>
        );
      default:
        return <p className="helper-text">Select an option to get started.</p>;
    }
  };

  return (
    <div className="summarizer-page">
      <h1 className="main-heading">Summarizer</h1>

      <div className="summary-options">
        <div className="option" onClick={() => setActiveOption('youtube')}>
          <h2>Summarize from YouTube</h2>
          <p>Paste a YouTube link to get a summary of the video content.</p>
        </div>
        <div className="option" onClick={() => setActiveOption('pdf')}>
          <h2>Summarize from PDF</h2>
          <p>Upload a PDF file and get a concise summary of the document.</p>
        </div>
        <div className="option" onClick={() => setActiveOption('text')}>
          <h2>Summarize from Text</h2>
          <p>Enter any text or paragraph you want summarized instantly.</p>
        </div>
        <div className="option" onClick={() => setActiveOption('news')}>
          <h2>Summarize from News Article</h2>
          <p>Provide a news link and receive a short summary of the article.</p>
        </div>
      </div>

      <div className="summary-input">
        {renderForm()}
        {outputText && (
          <div className="output-box">
            <h3>Summary Output:</h3>
            <p>{outputText}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default SummarizerPage;
