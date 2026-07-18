import { ClipboardList } from "lucide-react";

export default function EmptyComplaints() {
  return (
    <div className="rounded-xl border border-dashed border-paper-300 bg-paper-50 px-8 py-20 text-center">

      <ClipboardList
        size={54}
        className="mx-auto text-ink-300"
      />

      <h2 className="mt-6 text-2xl font-semibold text-ink-900">
        No complaints yet
      </h2>

      <p className="mt-2 text-ink-500">
        Once you submit a complaint,
        it will appear here.
      </p>

    </div>
  );
}