import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";

import { issueApi } from "./api";

export function usePendingIssues() {
  return useQuery({
    queryKey: ["pending-issues"],
    queryFn: issueApi.getPendingIssues,
  });
}

export function useIssueDetails(
  issueNumber: string
) {
  return useQuery({
    queryKey: ["issue", issueNumber],
    queryFn: () =>
      issueApi.getIssueByNumber(issueNumber),
    enabled: !!issueNumber,
  });
}

export function useAssignDepartment() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({
      issueNumber,
      departmentId,
    }: {
      issueNumber: string;
      departmentId: number;
    }) =>
      issueApi.assignDepartment(issueNumber, {
        department_id: departmentId,
      }),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["pending-issues"],
      });
    },
  });
}
export function useMyIssues() {
    return useQuery({
        queryKey: ["department-issues"],
        queryFn: issueApi.getMyIssues,
    });
}
export function useUpdateStatus() {

    const queryClient = useQueryClient();

    return useMutation({

        mutationFn: ({
            issueNumber,
            status,
        }: {
            issueNumber: string;
            status: string;
        }) =>
            issueApi.updateStatus(
                issueNumber,
                { status }
            ),

        onSuccess: () => {

            queryClient.invalidateQueries({
                queryKey: ["department-issues"],
            });

        },
    });
}
export function useDepartments() {

  return useQuery({

    queryKey: ["departments"],

    queryFn: issueApi.getDepartments,

  });

}

export function useDepartmentIssues(
  departmentId: number
) {

  return useQuery({

    queryKey: [
      "department-issues",
      departmentId,
    ],

    queryFn: () =>
      issueApi.getDepartmentIssues(
        departmentId
      ),

    enabled: !!departmentId,

  });

}
