import axiosInstance from "../../api/axios";
import { API_ENDPOINTS } from "../../api/endpoints";

import {
  type CitizenDashboardResponse,
  type MunicipalDashboardResponse,
  type DepartmentDashboardResponse,
} from "./types";

export async function getCitizenDashboard() {
  const response = await axiosInstance.get<{
    data: CitizenDashboardResponse;
  }>(API_ENDPOINTS.DASHBOARD.CITIZEN);

  return response.data.data;
}

export async function getMunicipalDashboard() {
  const response = await axiosInstance.get<{
    data: MunicipalDashboardResponse;
  }>(API_ENDPOINTS.DASHBOARD.MUNICIPAL);

  return response.data.data;
}

export async function getDepartmentDashboard() {
  const response = await axiosInstance.get<{
    data: DepartmentDashboardResponse;
  }>(API_ENDPOINTS.DASHBOARD.DEPARTMENT);

  return response.data.data;
}