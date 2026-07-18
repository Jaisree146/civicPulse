import { useQuery } from "@tanstack/react-query";

import {
  getCitizenDashboard,
  getMunicipalDashboard,
  getDepartmentDashboard,
} from "./api";

export function useCitizenDashboard() {
  return useQuery({
    queryKey: ["citizen-dashboard"],
    queryFn: getCitizenDashboard,
  });
}

export function useMunicipalDashboard() {
  return useQuery({
    queryKey: ["municipal-dashboard"],
    queryFn: getMunicipalDashboard,
  });
}

export function useDepartmentDashboard() {
  return useQuery({
    queryKey: ["department-dashboard"],
    queryFn: getDepartmentDashboard,
  });
}