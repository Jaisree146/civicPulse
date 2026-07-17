import api from "../../api/axios";
import { API_ENDPOINTS } from "../../api/endpoints";

import type {
  CreateComplaintRequest,
  CreateComplaintResponse,
  MyComplaintsResponse,
  ComplaintDetailsResponse,
} from "./types";

export const complaintApi = {
  create: async (
    data: CreateComplaintRequest
  ): Promise<CreateComplaintResponse> => {
    const response = await api.post(
      API_ENDPOINTS.COMPLAINTS.CREATE,
      data
    );

    return response.data.data;
  },

  getMyComplaints: async (): Promise<MyComplaintsResponse> => {
    const response = await api.get(
      API_ENDPOINTS.COMPLAINTS.MY
    );

    return response.data.data;
  },

  getComplaintByNumber: async (
    complaintNumber: string
  ): Promise<ComplaintDetailsResponse> => {
    const response = await api.get(
      API_ENDPOINTS.COMPLAINTS.DETAILS(
        complaintNumber
      )
    );

    return response.data.data;
  },
};