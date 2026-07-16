import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { AxiosError } from "axios";
import toast from "react-hot-toast";

import PriorityBadge from "../components/PriorityBadge";
import StatusBadge from "../components/StatusBadge";
import StatusSelector from "./components/StatusSelector";

import {
  useIssueDetails,
  useUpdateStatus,
} from "../hooks";

export default function DepartmentIssueDetails() {
  const { issueNumber } =
    useParams<{ issueNumber: string }>();

  const navigate = useNavigate();

  const {
    data: issue,
    isLoading,
    isError,
  } = useIssueDetails(issueNumber ?? "");

  const updateMutation = useUpdateStatus();

  const [status, setStatus] = useState("");

  useEffect(() => {
    if (issue) {
      setStatus(issue.status);
    }
  }, [issue]);

  if (isLoading) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        Loading...
      </div>
    );
  }

  if (isError || !issue) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        Failed to load issue.
      </div>
    );
  }

  // After this point issue is guaranteed to exist
  const {
    issue_number,
    summary,
    priority,
    category,
    status: currentStatus,
    assigned_department,
    report_count,
  } = issue;

  async function handleUpdate() {
    try {
      await updateMutation.mutateAsync({
        issueNumber: issue_number,
        status,
      });

      toast.success(
        "Issue status updated successfully."
      );

      navigate("/department/issues");
    } catch (error) {
      if (error instanceof AxiosError) {
        toast.error(
          error.response?.data?.message ??
            "Failed to update issue."
        );
      } else {
        toast.error("Something went wrong.");
      }
    }
  }

  return (
    <div className="space-y-8">

      <div>
        <h1 className="font-serif text-3xl font-bold text-ink-900">
          Issue Details
        </h1>

        <p className="mt-2 text-ink-500">
          Review issue information and update its status.
        </p>
      </div>

      <div className="rounded-xl border border-paper-200 bg-paper-50 p-8">

        <div className="flex justify-between">

          <div>
            <p className="font-mono text-xs uppercase tracking-widest text-ink-400">
              {issue_number}
            </p>

            <h2 className="mt-2 text-2xl font-semibold text-ink-900">
              {summary}
            </h2>
          </div>

          <PriorityBadge priority={priority} />

        </div>

        <div className="mt-8 grid gap-6 md:grid-cols-2">

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Category
            </p>

            <p className="mt-1">
              {category}
            </p>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Status
            </p>

            <div className="mt-2">
              <StatusBadge status={currentStatus} />
            </div>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Assigned Department
            </p>

            <p className="mt-1">
              {assigned_department}
            </p>
          </div>

          <div>
            <p className="text-xs uppercase tracking-wider text-ink-400">
              Report Count
            </p>

            <p className="mt-1">
              {report_count}
            </p>
          </div>

        </div>

        <div className="mt-10">
          <StatusSelector
            value={status}
            onChange={setStatus}
          />
        </div>

        <div className="mt-8 flex justify-end">

          <button
            onClick={handleUpdate}
            disabled={updateMutation.isPending}
            className="rounded-xl bg-navy-800 px-6 py-3 font-medium text-white transition hover:bg-navy-700 disabled:opacity-50"
          >
            {updateMutation.isPending
              ? "Updating..."
              : "Update Status"}
          </button>

        </div>

      </div>

    </div>
  );
}