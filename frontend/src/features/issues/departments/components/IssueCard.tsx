import {
  ArrowRight,
  CalendarDays,
  FolderKanban,
} from "lucide-react";
import { useNavigate } from "react-router-dom";

import type { Issue } from "../../types";

import PriorityBadge from "../../components/PriorityBadge";
import StatusBadge from "../../components/StatusBadge";

interface Props {
  issue: Issue;
  actionLabel: string;
  actionPath: string;
}

export default function IssueCard({
  issue,
  actionLabel,
  actionPath,
}: Props) {
  const navigate = useNavigate();

  const department =
    issue.assigned_department ??
    issue.suggested_department;

  return (
    <div className="rounded-xl border border-paper-200 bg-paper-50 p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">

      {/* Header */}

      <div className="flex items-start justify-between gap-4">

        <div className="min-w-0">

          <p className="font-mono text-xs uppercase tracking-widest text-ink-400">
            {issue.issue_number}
          </p>

          <h2 className="mt-2 line-clamp-2 text-xl font-semibold text-ink-900">
            {issue.summary}
          </h2>

        </div>

        <PriorityBadge priority={issue.priority} />

      </div>

      {/* Content */}

      <div className="mt-6 space-y-4">

        <div className="flex items-center gap-3">

          <FolderKanban
            size={18}
            className="text-navy-700"
          />

          <span className="text-sm text-ink-500">
            Category
          </span>

          <span className="ml-auto font-medium text-ink-900">
            {issue.category}
          </span>

        </div>

        <div className="flex items-center">

          <span className="text-sm text-ink-500">
            Status
          </span>

          <div className="ml-auto">
            <StatusBadge status={issue.status} />
          </div>

        </div>

        {department && (

          <div className="flex items-center">

            <span className="text-sm text-ink-500">
              Department
            </span>

            <span className="ml-auto rounded-lg bg-navy-50 px-3 py-1 text-sm font-medium text-navy-700">
              {department}
            </span>

          </div>

        )}

        <div className="flex items-center">

          <span className="text-sm text-ink-500">
            Reports
          </span>

          <span className="ml-auto rounded-lg bg-paper-200 px-3 py-1 text-sm font-medium text-ink-900">
            {issue.report_count}
          </span>

        </div>

        <div className="flex items-center gap-3">

          <CalendarDays
            size={18}
            className="text-gold-600"
          />

          <span className="text-sm text-ink-500">
            {new Date(issue.created_at).toLocaleDateString(
              "en-IN",
              {
                day: "2-digit",
                month: "short",
                year: "numeric",
              }
            )}
          </span>

        </div>

      </div>

      {/* Footer */}

      <div className="mt-6 border-t border-paper-200 pt-5">

        <button
          onClick={() => navigate(actionPath)}
          className="flex w-full items-center justify-center gap-2 rounded-lg bg-navy-800 px-4 py-3 font-medium text-white transition hover:bg-navy-700"
        >
          {actionLabel}

          <ArrowRight size={18} />
        </button>

      </div>

    </div>
  );
}