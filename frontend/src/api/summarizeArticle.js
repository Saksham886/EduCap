import axios from 'axios';
const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
export const summarizeArticle = async (url) => {
  const response = await axios.post(`${BASE_URL}/summarize_url`, { url });
  return response.data;
};
