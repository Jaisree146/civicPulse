import axiosInstance, { CLOUDFRONT_BASEURL } from "./axios";
import { tokenService } from "../services/tokenService";


axiosInstance.interceptors.request.use(
  (config) => {
    const token = tokenService.getToken();

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },

  (error) => Promise.reject(error),
);

import { API_ENDPOINTS } from "./endpoints";
import axios from "axios";

axiosInstance.interceptors.response.use(
  (response) => response,

  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
      
        const response = await axios.post(
         CLOUDFRONT_BASEURL+API_ENDPOINTS.AUTH.REFRESH,
          {},
          { withCredentials: true }
        );

        const newToken = response.data.data.access_token;

        tokenService.setToken(newToken);

        originalRequest.headers.Authorization = `Bearer ${newToken}`;

        return axiosInstance(originalRequest);
      } catch {
        tokenService.clearToken();

        window.location.href = "/login";
      }
    }

    return Promise.reject(error);
  },
);
