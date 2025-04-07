

// newer one

import React, { useState } from 'react';
import './Tts.css';

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
  );
};

export default FileUploader;


// import React, { useState } from "react";

// const TextToSpeechConverter = () => {
//   const [text, setText] = useState("");
//   const [fileName, setFileName] = useState("");
//   const [volume, setVolume] = useState(1); // Default volume is full (1.0)

//   let utterance = null;

//   const handleTextChange = (e) => {
//     setText(e.target.value);
//   };

//   const handleFileChange = (e) => {
//     const file = e.target.files[0];
//     if (file) {
//       setFileName(file.name);
//       const reader = new FileReader();
//       reader.onload = (event) => {
//         setText(event.target.result);
//       };
//       reader.readAsText(file);
//     }
//   };

//   const handleHoverSpeak = () => {
//     if (text.trim()) {
//       utterance = new SpeechSynthesisUtterance(text);
//       utterance.volume = volume;
//       utterance.lang = "en-US"; // You can change this to other languages
//       window.speechSynthesis.speak(utterance);
//     }
//   };

//   const handleStopSpeaking = () => {
//     window.speechSynthesis.cancel();
//   };

//   return (
//     <div className="uploader-container" role="main" aria-label="Text to Speech Converter">
//       <h2>Text to Speech Converter</h2>

//       <textarea
//         className="text-input"
//         placeholder="Enter your text or upload a file..."
//         value={text}
//         onChange={handleTextChange}
//         onMouseEnter={handleHoverSpeak}
//         onMouseLeave={handleStopSpeaking}
//         aria-label="Text input area for speech"
//         rows={8}
//         style={{ width: "100%", padding: "10px", fontSize: "16px", marginBottom: "10px" }}
//       />

//       <label htmlFor="file-upload" className="file-upload-label" style={{ display: "block", marginBottom: "10px" }}>
//         Upload File:
//         <input
//           id="file-upload"
//           type="file"
//           onChange={handleFileChange}
//           className="file-input"
//           aria-label="Upload a file to convert to speech"
//         />
//       </label>

//       {fileName && <p className="file-name">📄 Upload File: {fileName}</p>}

//       <div className="slider-container" style={{ marginTop: "10px" }}>
//         <label htmlFor="volume-range">
//           Volume:
//           <input
//             id="volume-range"
//             type="range"
//             min="0"
//             max="1"
//             step="0.1"
//             value={volume}
//             onChange={(e) => setVolume(parseFloat(e.target.value))}
//             aria-valuemin="0"
//             aria-valuemax="1"
//             aria-valuenow={volume}
//             aria-label="Volume control"
//             style={{ marginLeft: "10px" }}
//           />
//         </label>
//       </div>
//     </div>
//   );
// };

// export default TextToSpeechConverter;
