export interface Issue {
  id: number;

  issue_number: string;

  summary: string;

  category: string;

  priority: string;

  status: string;

  report_count: number;

  latitude: number;

  longitude: number;

  suggested_department: string | null;

  assigned_department: string | null;

  created_at: string;
}

export type PendingIssuesResponse = Issue[];

export type IssueDetailsResponse = Issue;

export interface AssignDepartmentRequest {
  department_id: number;
}

export interface UpdateStatusRequest {
  status: string;
}

export interface Department {
  id: number;

  department_name: string;

  description: string;
}
export type DepartmentsResponse = Department[];

export type DepartmentIssuesResponse = Issue[];