import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import FeaturePage from './components/FeaturePage.jsx'
import FrontPage from './components/FrontPage.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <FrontPage/>
    <FeaturePage />
    
  </StrictMode>,
)
