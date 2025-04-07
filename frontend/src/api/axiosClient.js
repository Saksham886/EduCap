import axios from "axios";

const axiosClient = axios.create({
  baseURL: "http://localhost:5000", // Or your deployed Flask backend
  withCredentials: true, // If using cookies for auth
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosClient;
