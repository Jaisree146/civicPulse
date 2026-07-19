import axiosInstance from "./axios";
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

axiosInstance.interceptors.response.use(
  (response) => response,

  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const BASEURL = window.location.origin;
        const response = await axiosInstance.post(
          BASEURL+API_ENDPOINTS.AUTH.REFRESH,
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
