import axios from 'axios';

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

export const summarizeYoutube = async (url) => {
  const response = await axios.post(`${BASE_URL}/summarize_youtube`, { url });
  return response.data;
};
