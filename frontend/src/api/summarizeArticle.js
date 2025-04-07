import axios from 'axios';

export const summarizeArticle = async (url) => {
  const response = await axios.post('/summarize_url', { url });
  return response.data;
};
