import type { Complaint } from "../../types";
import StatusBadge from "./StatusBadge";

interface Props {
  complaint: Complaint;
}

export default function ComplaintInfo({
  complaint,
}: Props) {
  return (
    <div className="rounded-xl border border-paper-200 bg-paper-50 p-8 shadow-sm">

      <div className="flex items-start justify-between">

        <div>

          <p className="font-mono text-xs uppercase tracking-widest text-ink-400">
            {complaint.complaint_number}
          </p>

          <h2 className="mt-2 text-3xl font-bold text-ink-900">
            {complaint.title}
          </h2>

        </div>

        <StatusBadge
          status={complaint.status}
        />

      </div>

      <div className="mt-8 space-y-6">

        <div>

          <h3 className="font-semibold text-ink-900">
            Description
          </h3>

          <p className="mt-2 leading-7 text-ink-600">
            {complaint.description}
          </p>

        </div>

        <div className="grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-xs uppercase tracking-widest text-ink-400">
              Latitude
            </p>

            <p className="mt-1 font-medium">
              {complaint.latitude}
            </p>

          </div>

          <div>

            <p className="text-xs uppercase tracking-widest text-ink-400">
              Longitude
            </p>

            <p className="mt-1 font-medium">
              {complaint.longitude}
            </p>

          </div>

          <div>

            <p className="text-xs uppercase tracking-widest text-ink-400">
              Submitted On
            </p>

            <p className="mt-1 font-medium">
              {new Date(
                complaint.created_at
              ).toLocaleString()}
            </p>

          </div>

        </div>

      </div>

    </div>
  );
}