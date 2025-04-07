// src/api/ChatBot.js
import axios from 'axios';

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

export const Text = async (input) => {
  const res = await axios.post(`${BASE_URL}/chat`, { input });
  return res.data;
};
