import api from "../../api/axios";
import { API_ENDPOINTS } from "../../api/endpoints";

import type {
  PendingIssuesResponse,
  IssueDetailsResponse,
  AssignDepartmentRequest,
  Department,
  UpdateStatusRequest,
  Issue,
} from "./types";

export const issueApi = {
  getPendingIssues: async (): Promise<PendingIssuesResponse> => {
    const response = await api.get(
      API_ENDPOINTS.ISSUES.PENDING
    );

    return response.data.data;
  },

  getIssueByNumber: async (
    issueNumber: string
  ): Promise<IssueDetailsResponse> => {
    const response = await api.get(
      API_ENDPOINTS.ISSUES.DETAILS(issueNumber)
    );

    return response.data.data;
  },

  assignDepartment: async (
    issueNumber: string,
    data: AssignDepartmentRequest
  ) => {
    const response = await api.put(
      API_ENDPOINTS.ISSUES.ASSIGN(issueNumber),
      data
    );

    return response.data.data;
  },

  getMyIssues: async (): Promise<PendingIssuesResponse> => {
    const response = await api.get(
      API_ENDPOINTS.ISSUES.MY
    );

    return response.data.data;
  },

  updateStatus: async (
    issueNumber: string,
    data: UpdateStatusRequest
  ) => {
    const response = await api.put(
      API_ENDPOINTS.ISSUES.STATUS(issueNumber),
      data
    );

    return response.data.data;
  },
  getDepartments: async (): Promise<Department[]> => {

  const response = await api.get(
    API_ENDPOINTS.DEPARTMENTS.ALL
  );

  return response.data.data;

},

getDepartmentIssues: async (
  departmentId: number
): Promise<Issue[]> => {

  const response = await api.get(
    API_ENDPOINTS.DEPARTMENTS.ISSUES(
      departmentId
    )
  );

  return response.data.data;

},
};
