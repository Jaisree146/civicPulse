export interface User {
  id: number;
  full_name: string;
  role: string;
}

export interface AuthContextType {
  user: User | null;

  accessToken: string | null;

  login: (token: string, user: User) => void;

  logout: () => void;

  updateAccessToken: (token: string) => void;

  isAuthenticated: boolean;

  isLoading: boolean;
}
