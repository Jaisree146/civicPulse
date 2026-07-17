import { ClipboardCheck } from "lucide-react";

import { usePendingIssues } from "../hooks";
import IssueCard from "./components/IssueCard";

export default function PendingIssues() {
  const {
    data: issues,
    isLoading,
    isError,
  } = usePendingIssues();

  if (isLoading) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        <p className="text-ink-500">
          Loading pending issues...
        </p>
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        <p className="text-red-600">
          Failed to load pending issues.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-8">

      {/* Header */}

      <div>
        <h1 className="font-serif text-3xl font-bold text-ink-900">
          Pending Review
        </h1>

        <p className="mt-2 text-ink-500">
          Review AI suggested departments before assigning
          issues to the appropriate department.
        </p>
      </div>

      {/* Empty State */}

      {issues?.length === 0 && (
        <div className="rounded-xl border border-dashed border-paper-300 bg-paper-50 px-8 py-20 text-center">
          <ClipboardCheck
            size={60}
            className="mx-auto text-ink-300"
          />

          <h2 className="mt-6 text-2xl font-semibold text-ink-900">
            No Pending Issues
          </h2>

          <p className="mt-2 text-ink-500">
            Every issue has already been reviewed and assigned.
          </p>
        </div>
      )}

      {/* Cards */}

      {issues && issues.length > 0 && (
        <div className="grid gap-6 lg:grid-cols-2">
          {issues.map((issue) => (
            <IssueCard
              key={issue.issue_number}
              issue={issue}
              actionLabel="Review Assignment"
              actionPath={`/municipal/issues/${issue.issue_number}`}
            />
          ))}
        </div>
      )}

    </div>
  );
}