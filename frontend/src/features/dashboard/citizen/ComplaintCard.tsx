import type { RecentComplaint } from "../types";

interface Props {
  complaint: RecentComplaint;
}

const STATUS_STYLES: Record<
  string,
  { dot: string; text: string; bg: string; border: string }
> = {
  Resolved: {
    dot: "bg-[#2f6f4f]",
    text: "text-[#2f6f4f]",
    bg: "bg-[#eaf3ee]",
    border: "border-[#cfe3d8]",
  },
  Pending: {
    dot: "bg-gold-600",
    text: "text-gold-600",
    bg: "bg-[#f7ecd9]",
    border: "border-[#ecdcb8]",
  },
  "In Progress": {
    dot: "bg-navy-700",
    text: "text-navy-700",
    bg: "bg-[#e7edf5]",
    border: "border-[#d3ddec]",
  },
};

const DEFAULT_STATUS_STYLE = {
  dot: "bg-ink-400",
  text: "text-ink-600",
  bg: "bg-paper-200",
  border: "border-paper-200",
};

function StatusTag({ status }: { status: string }) {
  const style = STATUS_STYLES[status] ?? DEFAULT_STATUS_STYLE;

  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 font-mono text-[10px] font-semibold uppercase tracking-wider ${style.bg} ${style.text} ${style.border}`}
    >
      <span className={`h-1.5 w-1.5 rounded-full ${style.dot}`} />
      {status}
    </span>
  );
}

export default function ComplaintCard({ complaint }: Props) {
  return (
    <div className="rounded-xl border border-paper-200 bg-paper-50 p-5 transition-all hover:border-paper-300 hover:shadow-md">
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0 flex-1">
          <p className="font-mono text-[11px] uppercase tracking-wider text-ink-400">
            Complaint #{complaint.complaint_number}
          </p>

          <h3 className="mt-2 text-lg font-semibold text-ink-900 line-clamp-2">
            {complaint.title}
          </h3>
        </div>

        <StatusTag status={complaint.status} />
      </div>
    </div>
  );
}