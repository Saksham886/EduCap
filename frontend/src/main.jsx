import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import './index.css';
import FeaturePage from './components/FeaturePage.jsx';
import FrontPage from './components/FrontPage.jsx';
import SummarizerPage from './components/SummarizerPage.jsx'; // import the component
import FileUploader from './components/tts.jsx';
import Header from './components/NavBar.jsx';
import ChatBox from './components/Cb.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<><FrontPage /><FeaturePage /></>} />
        <Route path="/summarizer" element={<SummarizerPage />} />
        <Route path="/text_to_speech" element={<FileUploader />} />
        <Route path="/ChatBot" element={<ChatBox />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);

