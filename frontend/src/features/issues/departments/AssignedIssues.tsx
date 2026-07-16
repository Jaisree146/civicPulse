import { Briefcase } from "lucide-react";

import { useMyIssues } from "../hooks";

import IssueCard from "./components/IssueCard";

export default function AssignedIssues() {
  const {
    data: issues,
    isLoading,
    isError,
  } = useMyIssues();

  if (isLoading) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        <p className="text-ink-500">
          Loading assigned issues...
        </p>
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        <p className="text-red-600">
          Failed to load assigned issues.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-8">

      <div>

        <h1 className="font-serif text-3xl font-bold text-ink-900">
          Assigned Issues
        </h1>

        <p className="mt-2 text-ink-500">
          View and update issues assigned to your department.
        </p>

      </div>

      {issues && issues.length === 0 && (

        <div className="rounded-xl border border-dashed border-paper-300 bg-paper-50 px-8 py-20 text-center">

          <Briefcase
            size={60}
            className="mx-auto text-ink-300"
          />

          <h2 className="mt-6 text-2xl font-semibold text-ink-900">
            No Assigned Issues
          </h2>

          <p className="mt-2 text-ink-500">
            New issues assigned to your department will appear here.
          </p>

        </div>

      )}

      {issues && issues.length > 0 && (

        <div className="grid gap-6 lg:grid-cols-2">

          {issues.map((issue) => (

            <IssueCard
  key={issue.issue_number}
  issue={issue}
  actionLabel="Update Status"
  actionPath={`/department/issues/${issue.issue_number}`}
/>

          ))}

        </div>

      )}

    </div>
  );
}