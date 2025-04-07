// Example: Summarize text
import axios from 'axios';
const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
export const summarizeText = async (text, input_lang = "en", return_lang = "en") => {
    const res = await axios.post(`${BASE_URL}/summarize`, {
      text, input_lang, return_lang
    });
    return res.data;
  };
  