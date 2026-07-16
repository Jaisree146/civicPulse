export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;

  user: {
    id: number;
    full_name: string;
    role: string;
  };
}
export interface RegisterRequest {
  full_name: string;
  email: string;
  password: string;
  phone: string;
}

export interface ChangePasswordRequest {
  old_password: string;
  new_password: string;
  confirm_password: string;
}