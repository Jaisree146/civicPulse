import {
  ClipboardList,
  Clock3,
  Wrench,
  CircleCheckBig,
} from "lucide-react";

import StatCard from "../components/StatCard";
import StatusChart from "./components/StatusChart";
import { useDepartmentDashboard } from "../hooks";

export default function DepartmentDashboard() {
  const {
    data,
    isLoading,
    isError,
  } = useDepartmentDashboard();

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
    <div className="space-y-10">
      <div>
        <h1 className="text-3xl font-bold text-ink-900">
          Department Dashboard
        </h1>

        <p className="mt-2 text-ink-500">
          Track assigned issues and monitor their resolution.
        </p>
      </div>

      <section className="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="Assigned"
          value={data.assigned}
          icon={<ClipboardList size={24} />}
        />

        <StatCard
          title="Pending"
          value={data.pending}
          icon={<Clock3 size={24} />}
        />

        <StatCard
          title="In Progress"
          value={data.in_progress}
          icon={<Wrench size={24} />}
        />

        <StatCard
          title="Resolved"
          value={data.resolved}
          icon={<CircleCheckBig size={24} />}
        />
      </section>

      <StatusChart
        assigned={data.pending}
        inProgress={data.in_progress}
        resolved={data.resolved}
      />
    </div>
  );
}