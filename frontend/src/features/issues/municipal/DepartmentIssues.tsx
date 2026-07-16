import { useParams } from "react-router-dom";

import { Briefcase } from "lucide-react";

import { useDepartmentIssues } from "../hooks";

import IssueCard from "./components/IssueCard";

export default function DepartmentIssues() {

  const { departmentId } = useParams();

  const {
    data: issues,
    isLoading,
    isError,
  } = useDepartmentIssues(
    Number(departmentId)
  );

  if (isLoading) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        Loading issues...
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex h-[70vh] items-center justify-center text-red-600">
        Failed to load issues.
      </div>
    );
  }

  return (

    <div className="space-y-8">

      <div>

        <h1 className="font-serif text-3xl font-bold text-ink-900">
          Department Issues
        </h1>

        <p className="mt-2 text-ink-500">
          Issues assigned to this department.
        </p>

      </div>

      {issues && issues.length === 0 && (

        <div className="rounded-xl border border-dashed border-paper-300 bg-paper-50 px-8 py-20 text-center">

          <Briefcase
            size={60}
            className="mx-auto text-ink-300"
          />

          <h2 className="mt-6 text-2xl font-semibold text-ink-900">
            No Issues Assigned
          </h2>

        </div>

      )}

      {issues && issues.length > 0 && (

        <div className="grid gap-6 lg:grid-cols-2">

          {issues.map((issue) => (

            <IssueCard

              key={issue.issue_number}

              issue={issue}

              actionLabel="View Details"

              actionPath={`/municipal/issues/${issue.issue_number}`}

            />

          ))}

        </div>

      )}

    </div>

  );
}