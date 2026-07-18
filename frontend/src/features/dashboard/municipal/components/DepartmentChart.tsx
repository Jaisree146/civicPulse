import {
  ResponsiveContainer,
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Bar,
} from "recharts";

import type { DepartmentSummary } from "../../types";

interface Props {
  data: DepartmentSummary[];
}

export default function DepartmentChart({
  data,
}: Props) {
  return (
    <div className="rounded-xl border border-paper-200 bg-paper-50 p-6 shadow-sm">
      <div className="mb-6">
        <h2 className="text-xl font-semibold text-ink-900">
          Issues by Department
        </h2>

        <p className="mt-1 text-sm text-ink-500">
          Distribution of issues assigned across departments.
        </p>
      </div>

      <div className="h-96">
        <ResponsiveContainer
          width="100%"
          height="100%"
        >
          <BarChart
            data={data}
            layout="vertical"
            margin={{
              top: 5,
              right: 20,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis type="number" />

            <YAxis
              type="category"
              dataKey="department"
              width={120}
            />

            <Tooltip />

            <Bar
              dataKey="count"
              radius={[0, 8, 8, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}