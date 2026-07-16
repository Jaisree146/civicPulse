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

  return (

    <div className="rounded-xl border border-paper-200 bg-paper-50 p-5 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">

      <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">

        <div className="min-w-0 flex-1">

          <p className="font-mono text-xs uppercase tracking-widest text-ink-400">
            {issue.issue_number}
          </p>

          <h2 className="mt-2 break-words text-xl font-semibold text-ink-900">
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
            className="shrink-0 text-navy-700"
          />

          <span className="text-sm text-ink-500">
            Category
          </span>

          <span className="ml-auto text-right font-medium text-ink-900 break-words">
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

        {issue.suggested_department && (

          <div className="flex items-center">

            <span className="text-sm text-ink-500">
              AI Suggested
            </span>

            <span className="ml-auto rounded-lg bg-navy-50 px-3 py-1 text-sm font-medium text-navy-700">
              {issue.suggested_department}
            </span>

          </div>

        )}

        {issue.assigned_department && (

          <div className="flex items-center">

            <span className="text-sm text-ink-500">
              Assigned
            </span>

            <span className="ml-auto rounded-lg bg-green-50 px-3 py-1 text-sm font-medium text-green-700">
              {issue.assigned_department}
            </span>

          </div>

        )}

        <div className="flex items-center gap-3">

          <CalendarDays
            size={18}
            className="shrink-0 text-gold-600"
          />

          <span className="text-sm text-ink-500">
            {new Date(issue.created_at).toLocaleString()}
          </span>

        </div>

      </div>

      {/* Footer */}

      <div className="mt-6 border-t border-paper-200 pt-5">

        <button
          onClick={() => navigate(actionPath)}
          className="flex w-full items-center justify-center gap-2 rounded-lg bg-navy-800 px-4 py-3 font-medium text-paper-50 transition hover:bg-navy-700"
        >

          {actionLabel}

          <ArrowRight size={18} />

        </button>

      </div>

    </div>

  );

}