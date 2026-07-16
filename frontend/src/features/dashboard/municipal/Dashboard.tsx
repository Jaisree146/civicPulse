import {
  ClipboardList,
  Clock3,
  UserCheck,
  Wrench,
  CircleCheckBig,
} from "lucide-react";

import StatCard from "../components/StatCard";
import { useMunicipalDashboard } from "../hooks";
import DepartmentChart from "./components/DepartmentChart";

export default function MunicipalDashboard() {
  const {
    data,
    isLoading,
    isError,
  } = useMunicipalDashboard();

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
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-ink-900">
          Municipal Dashboard
        </h1>

        <p className="mt-2 text-ink-500">
          Monitor civic issues and oversee department assignments.
        </p>
      </div>

      {/* Statistics */}
      <section className="grid gap-6 sm:grid-cols-2 xl:grid-cols-5">
        <StatCard
          title="Total Issues"
          value={data.total_issues}
          icon={<ClipboardList size={24} />}
        />

        <StatCard
          title="Pending Review"
          value={data.pending_review}
          icon={<Clock3 size={24} />}
        />

        <StatCard
          title="Assigned"
          value={data.assigned}
          icon={<UserCheck size={24} />}
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

      {/* Department Distribution */}
      <DepartmentChart
        data={data.department_summary}
      />
    </div>
  );
}