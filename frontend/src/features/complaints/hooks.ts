import {
  useMutation,
  useQuery,
} from "@tanstack/react-query";

import { complaintApi } from "./api";

export function useCreateComplaint() {
  return useMutation({
    mutationFn: complaintApi.create,
  });
}

export function useMyComplaints() {
  return useQuery({
    queryKey: ["my-complaints"],
    queryFn: complaintApi.getMyComplaints,
  });
}

export function useComplaintDetails(
  complaintNumber: string
) {
  return useQuery({
    queryKey: [
      "complaint",
      complaintNumber,
    ],
    queryFn: () =>
      complaintApi.getComplaintByNumber(
        complaintNumber
      ),
    enabled: !!complaintNumber,
  });
}