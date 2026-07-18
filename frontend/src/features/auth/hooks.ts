import { useMutation } from "@tanstack/react-query";

import {
  login,
  register,
  logout,
  changePassword,
} from "./api";

import {
  type LoginRequest,
  type LoginResponse,
  type RegisterRequest,
  type ChangePasswordRequest,
} from "./types";

export function useLogin() {
  return useMutation<LoginResponse, Error, LoginRequest>({
    mutationFn: login,
  });
}

export function useRegister() {
  return useMutation<void, Error, RegisterRequest>({
    mutationFn: register,
  });
}

export function useLogout() {
  return useMutation<void, Error>({
    mutationFn: logout,
  });
}

export function useChangePassword() {
  return useMutation<void, Error, ChangePasswordRequest>({
    mutationFn: changePassword,
  });
}