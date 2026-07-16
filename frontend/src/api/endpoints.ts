export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: "/api/auth/login",

    REGISTER: "/api/auth/register",

    REFRESH: "/api/auth/refresh",

    LOGOUT: "/api/auth/logout",

    CHANGE_PASSWORD: "/api/auth/change-password",
  },

  DASHBOARD: {
    CITIZEN: "/api/dashboard/citizen",

    MUNICIPAL: "/api/dashboard/municipal",

    DEPARTMENT: "/api/dashboard/department",
  },

  COMPLAINTS: {
    CREATE: "/api/complaints",

    MY: "/api/complaints/my",

    DETAILS: (id: number) => `/api/complaints/${id}`,
  },

  ISSUES: {
    ALL: "/api/issues",

    PENDING: "/api/issues/pending",

    MY: "/api/issues/my",

    ASSIGN: (id: number) => `/api/issues/${id}/assign`,

    STATUS: (id: number) => `/api/issues/${id}/status`,
  },

  CHAT: {
    SEND: "/api/chat",
  },
};
