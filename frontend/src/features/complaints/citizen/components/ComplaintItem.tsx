import { ChevronRight } from "lucide-react";
import { useNavigate } from "react-router-dom";
import {
  COMPLAINT_STATUS_STYLES,
  DEFAULT_STATUS_STYLE,
} from "../../constants";
import type { Complaint } from "../../types";

interface Props {
  complaint: Complaint;
}


export default function ComplaintItem({
  complaint,
}: Props) {
  const navigate = useNavigate();

  const style =
  COMPLAINT_STATUS_STYLES[
    complaint.status
  ] ?? DEFAULT_STATUS_STYLE;

  return (
    <div className="rounded-xl border border-paper-200 bg-paper-50 p-6 shadow-sm transition hover:shadow-md">
      <div className="flex items-start justify-between">

        <div>

          <p className="font-mono text-xs tracking-widest text-ink-400">
            {complaint.complaint_number}
          </p>

          <h3 className="mt-1 text-lg font-semibold text-ink-900">
            {complaint.title}
          </h3>

          <p className="mt-2 line-clamp-2 text-sm text-ink-500">
            {complaint.description}
          </p>

          <p className="mt-4 text-xs text-ink-400">
            Created on{" "}
            {new Date(
              complaint.created_at
            ).toLocaleDateString()}
          </p>

        </div>

        <span
          className={`inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-semibold ${style.bg} ${style.border} ${style.text}`}
        >
          <span
            className={`h-2 w-2 rounded-full ${style.dot}`}
          />
          {complaint.status}
        </span>

      </div>

      <div className="mt-5 border-t border-paper-200 pt-4">

        <button
          onClick={() =>
            navigate(
              `/citizen/complaints/${complaint.complaint_number}`
            )
          }
          className="flex items-center gap-1 text-sm font-medium text-navy-700 hover:text-gold-600"
        >
          View Details

          <ChevronRight size={18} />
        </button>

      </div>
    </div>
  );
}