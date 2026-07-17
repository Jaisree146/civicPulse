import ComplaintCard from "./ComplaintCard";

import type { RecentComplaint } from "../types";

interface Props {
  complaints: RecentComplaint[];
}

export default function RecentComplaints({ complaints }: Props) {
  return (
    <section className="space-y-5">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="font-serif text-xl font-semibold text-ink-900">
            Recent Complaints
          </h2>
          <p className="mt-0.5 font-mono text-[11px] uppercase tracking-wider text-ink-400">
            Latest activity
          </p>
        </div>
      </div>

      {complaints.length === 0 ? (
        <div className="rounded-lg border border-dashed border-paper-200 bg-paper-50 py-14 text-center">
          <p className="text-sm text-ink-400">No complaints found.</p>
        </div>
      ) : (
        <div className="grid gap-4 lg:grid-cols-2">
          {complaints.map((complaint) => (
            <ComplaintCard
              key={complaint.complaint_number}
              complaint={complaint}
            />
          ))}
        </div>
      )}
    </section>
  );
}
