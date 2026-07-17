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
    DETAILS: (complaintNumber: string) =>
        `/api/complaints/${complaintNumber}`,
},

  ISSUES: {
    ALL: "/api/issues",
    PENDING: "/api/issues/pending",

    DETAILS: (issueNumber: string) =>
        `/api/issues/${issueNumber}`,

    ASSIGN: (issueNumber: string) =>
        `/api/issues/${issueNumber}/assign`,

     MY: "/api/issues/my",

    STATUS: (issueNumber: string) =>
        `/api/issues/${issueNumber}/status`,

},

DEPARTMENTS: {
  ALL: "/api/departments",

  ISSUES: (departmentId: number) =>
    `/api/departments/${departmentId}/issues`,
},

  CHAT: {
    CHAT: "/api/chat",
  },
};
