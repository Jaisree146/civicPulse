import axiosInstance from "../../api/axios";
import { API_ENDPOINTS } from "../../api/endpoints";

import {
    type LoginRequest,
    type LoginResponse,
    type RegisterRequest,
    type ChangePasswordRequest
} from "./types";

export async function login(
    data: LoginRequest
): Promise<LoginResponse>{

    const response =
        await axiosInstance.post(

            API_ENDPOINTS.AUTH.LOGIN,

            data

        );

    return response.data.data;
}

export async function register(
  data: RegisterRequest
) {
  const response = await axiosInstance.post(
    API_ENDPOINTS.AUTH.REGISTER,
    data
  );

  return response.data.data;
}

export async function changePassword(data: ChangePasswordRequest) {
  const response = await axiosInstance.put(
    API_ENDPOINTS.AUTH.CHANGE_PASSWORD,
    data
  );
  return response.data;
}
export async function logout(): Promise<void> {
  await axiosInstance.post(API_ENDPOINTS.AUTH.LOGOUT);
}