import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { AxiosError } from "axios";
import toast from "react-hot-toast";

import PriorityBadge from "../components/PriorityBadge";
import StatusBadge from "../components/StatusBadge";
import DepartmentSelector from "./components/DepartmentSelector";

import { useAssignDepartment, useDepartments, useIssueDetails } from "../hooks";

export default function MunicipalIssueDetails() {
  const { issueNumber } = useParams();

  const navigate = useNavigate();

  const { data: issue, isLoading } = useIssueDetails(issueNumber ?? "");

  const { data: departments } = useDepartments();

  const assignMutation = useAssignDepartment();

  const [selectedDepartment, setSelectedDepartment] = useState<number | "">("");

  useEffect(() => {
    if (issue && departments) {
      const department = departments.find(
        (d) => d.department_name === issue.suggested_department,
      );

      if (department) {
        setSelectedDepartment(department.id);
      }
    }
  }, [issue, departments]);

  if (isLoading || !issue) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        Loading...
      </div>
    );
  }

  const handleAssign = async () => {
    if (selectedDepartment === "") {
      toast.error("Please select a department.");
      return;
    }

    try {
      await assignMutation.mutateAsync({
        issueNumber: issue.issue_number,
        departmentId: selectedDepartment,
      });

      toast.success("Issue assigned successfully.");

      navigate("/municipal/issues");
    } catch (error) {
      if (error instanceof AxiosError) {
        toast.error(error.response?.data?.message ?? "Assignment failed.");
      } else {
        toast.error("Something went wrong.");
      }
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-serif text-3xl font-bold text-ink-900">
          Review Issue
        </h1>

        <p className="mt-2 text-ink-500">
          Verify the AI suggestion before assigning the issue.
        </p>
      </div>

      <div className="rounded-xl border border-paper-200 bg-paper-50 p-8 shadow-sm">
        <div className="flex items-start justify-between">
          <div>
            <p className="font-mono text-xs uppercase tracking-widest text-ink-400">
              {issue.issue_number}
            </p>

            <h2 className="mt-2 text-2xl font-semibold">{issue.summary}</h2>
          </div>

          <PriorityBadge priority={issue.priority} />
        </div>

        <div className="mt-8 grid gap-6 md:grid-cols-2">
          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Category
            </p>

            <p className="mt-1 font-medium">{issue.category}</p>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Status
            </p>

            <div className="mt-2">
              <StatusBadge status={issue.status} />
            </div>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              AI Suggested Department
            </p>

            <p className="mt-1 font-semibold text-navy-700">
              {issue.suggested_department}
            </p>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Report Count
            </p>

            <p className="mt-1 font-medium">{issue.report_count}</p>
          </div>
          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Latitude
            </p>

            <p className="mt-1 font-medium">{issue.latitude.toFixed(6)}</p>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Longitude
            </p>

            <p className="mt-1 font-medium">{issue.longitude.toFixed(6)}</p>
          </div>
        </div>

        <div className="mt-10">
          <DepartmentSelector
            departments={departments ?? []}
            selectedDepartment={selectedDepartment}
            onChange={setSelectedDepartment}
          />
        </div>

        <div className="mt-8 flex justify-end">
          <button
            onClick={handleAssign}
            disabled={assignMutation.isPending}
            className="rounded-xl bg-navy-800 px-6 py-3 font-medium text-white transition hover:bg-navy-700 disabled:opacity-50"
          >
            {assignMutation.isPending ? "Assigning..." : "Assign Department"}
          </button>
        </div>
      </div>
    </div>
  );
}
