import { useMutation } from "@tanstack/react-query";

import { login, register, changePassword } from "./api";

import {
  type LoginRequest,
  type LoginResponse,
  type RegisterRequest,
  type ChangePasswordRequest
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

export function useChangePassword() {
  return useMutation<void, Error, ChangePasswordRequest>({
    mutationFn: changePassword,
  });
}