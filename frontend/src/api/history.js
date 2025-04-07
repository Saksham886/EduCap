export const getUserHistory = async () => {
    const token = localStorage.getItem("token");
  
    const res = await axiosClient.get("/history", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
  
    return res.data;
  };
  