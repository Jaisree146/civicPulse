import axios from "axios";
export const CLOUDFRONT_BASEURL = window.location.origin;
const axiosInstance = axios.create({
  // Use the current application's origin so frontend API requests go through the same CloudFront domain.
  // CloudFront routes API paths (e.g., /api/*) to the backend based on its behavior configuration.
  //This is the work around for resolving the HTTPS constraint in ALB
  //baseURL: import.meta.env.VITE_API_BASE_URL,
  baseURL: CLOUDFRONT_BASEURL,

  withCredentials: true,

  headers: {
    "Content-Type": "application/json",
  },
});


export default axiosInstance;
