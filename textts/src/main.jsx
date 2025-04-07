import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import FileUploader from './components/tts'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <FileUploader/>
  </StrictMode>,
)
