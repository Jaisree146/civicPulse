import { createContext, type ReactNode, useState, useEffect } from "react";

import { type AuthContextType, type User } from "../types/auth";

import { tokenService } from "../services/tokenService";

import axios from "axios";
import { API_ENDPOINTS } from "../api/endpoints";

export const AuthContext = createContext<AuthContextType | null>(null);

interface Props {
  children: ReactNode;
}

export function AuthProvider({ children }: Props) {
  const [user, setUser] = useState<User | null>(null);

  const [accessToken, setAccessToken] = useState<string | null>(null);

  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const restoreSession = async () => {
      try {
        const response = await axios.post(
          import.meta.env.VITE_API_BASE_URL + API_ENDPOINTS.AUTH.REFRESH,
          {},
          { withCredentials: true }
        );
        const { access_token, user: userData } = response.data.data;
        setAccessToken(access_token);
        setUser(userData);
        tokenService.setToken(access_token);
      } catch (error) {    
  setAccessToken(null);
  setUser(null);
  tokenService.clearToken();

      } finally {
        setIsLoading(false);
      }
    };
    restoreSession();
  }, []);

  const login = (token: string, userData: User) => {
    setAccessToken(token);

    setUser(userData);

    tokenService.setToken(token);
  };
  const logout = () => {
    setAccessToken(null);

    setUser(null);

    tokenService.clearToken();
  };
  const updateAccessToken = (token: string) => {
    setAccessToken(token);

    tokenService.setToken(token);
  };
  return (
    <AuthContext.Provider
      value={{
        user,
        accessToken,
        login,
        logout,
        updateAccessToken,
        isAuthenticated: accessToken !== null,
        isLoading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}
