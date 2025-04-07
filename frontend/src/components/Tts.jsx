

// newer one
import Header from './NavBar';
import React, { useState } from 'react';
import './Tts.css';
import Footer from './Footer';
const FileUploader = () => {
  const [text, setText] = useState('');
  const [fileName, setFileName] = useState('');
  const [volume, setVolume] = useState(1);
  const [rate, setRate] = useState(1);

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
      const reader = new FileReader();
      reader.onload = (event) => {
        setText(event.target.result);
      };
      reader.readAsText(file);
    }
  };

  const speakText = () => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.volume = volume;
    utterance.rate = rate;
    window.speechSynthesis.speak(utterance);
  };

  return (
    <>
    <Header/>
    
    <div className="uploader-container">
      <h2>Text to Speech Converter</h2>

      <textarea
        className="text-input"
        placeholder="Enter your text or upload a file..."
        value={text}
        onChange={handleTextChange}
      />

      <label htmlFor="file-upload" className="file-upload-label">
        <input
          id="file-upload"
          type="file"
          onChange={handleFileChange}
          className="file-input"
        />
      </label>

      {fileName && <p className="file-name">📄 Upload File : {fileName}</p>}

      <div className="slider-container">
      <label>
  Volume:
  <input
    type="range"
    min="0"
    max="1"
    step="0.1"
    value={volume}
    onChange={(e) => setVolume(parseFloat(e.target.value))}
  />
</label>


        <label>
          Speed:
          <input
            type="range"
            min="0.5"
            max="2"
            step="0.1"
            value={rate}
            onChange={(e) => setRate(parseFloat(e.target.value))}
          />
        </label>
      </div>

      <button className="speak-button" onClick={speakText}>
        <b>🔊 Convert to Speech</b>
      </button>
    </div>
    <Footer/>
    </>
  );
};

export default FileUploader;


