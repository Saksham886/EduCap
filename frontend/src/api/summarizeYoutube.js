import axios from 'axios';

export const summarizeYoutube = async (url) => {
  const response = await axios.post('/summarize_youtube', { url });
  return response.data;
};
