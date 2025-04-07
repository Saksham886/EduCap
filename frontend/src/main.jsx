import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import './index.css';
import FeaturePage from './components/FeaturePage.jsx';
import FrontPage from './components/FrontPage.jsx';
import SummarizerPage from './components/SummarizerPage.jsx'; // import the component

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<><FrontPage /><FeaturePage /></>} />
        <Route path="/summarizer" element={<SummarizerPage />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);

