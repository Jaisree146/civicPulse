export interface RecentComplaint {
  complaint_number: string;
  title: string;
  status: string;
}

export interface CitizenDashboardResponse {
  total_complaints: number;
  resolved_complaints: number;
  recent_complaints: RecentComplaint[];
}

export interface DepartmentSummary {
  department: string;
  count: number;
}

export interface MunicipalDashboardResponse {
  total_issues: number;
  pending_review: number;
  assigned: number;
  in_progress: number;
  resolved: number;
  department_summary: DepartmentSummary[];
}

export interface DepartmentDashboardResponse {
  assigned: number;
  pending: number;
  in_progress: number;
  resolved: number;
}