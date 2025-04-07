import axios from 'axios';

export const summarizePdf = async (formData) => {
  const response = await axios.post('/summarize_pdf', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};
