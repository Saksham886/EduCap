// src/api/auth.js
import axiosClient from "./axiosClient";

export const signup = async (email, password) => {
  const res = await axiosClient.post("/signup", { email, password });
  return res.data;
};

export const login = async (email, password) => {
  const res = await axiosClient.post("/login", { email, password });
  return res.data;
};
