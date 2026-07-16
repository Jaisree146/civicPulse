import { ClipboardList, CircleCheckBig } from "lucide-react";

import StatCard from "../components/StatCard";
import RecentComplaints from "./RecentComplaints";
import { useCitizenDashboard } from "../hooks";

export default function CitizenDashboard() {
  const {
    data,
    isLoading,
    isError,
  } = useCitizenDashboard();

  if (isLoading) {
    return (
      <div className="flex h-full items-center justify-center">
        Loading dashboard...
      </div>
    );
  }

  if (isError || !data) {
    return (
      <div className="flex h-full items-center justify-center text-red-500">
        Failed to load dashboard.
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold text-ink-900">
          Citizen Dashboard
        </h1>

        <p className="mt-2 text-ink-500">
          Monitor your complaints and track their progress.
        </p>
      </div>

      <section className="grid gap-6 md:grid-cols-2">
        <StatCard
          title="Total Complaints"
          value={data.total_complaints}
          icon={<ClipboardList size={24} />}
        />

        <StatCard
          title="Resolved Complaints"
          value={data.resolved_complaints}
          icon={<CircleCheckBig size={24} />}
        />
      </section>

      <RecentComplaints
        complaints={data.recent_complaints}
      />
    </div>
  );
}