export const getAudio = async (text, lang = "en") => {
    const res = await axiosClient.post("/tts", { text, lang }, {
      responseType: "blob"
    });
  
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "summary.mp3");
    document.body.appendChild(link);
    link.click();
  };
  