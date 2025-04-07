// Example: Summarize text
export const summarizeText = async (text, input_lang = "en", return_lang = "en") => {
    const res = await axiosClient.post("/summarize", {
      text, input_lang, return_lang
    });
    return res.data;
  };
  