import {
  PieChart,
  Pie,
  Tooltip,
  Cell,
  ResponsiveContainer,
  Legend,
} from "recharts";

interface Props {
  assigned: number;
  inProgress: number;
  resolved: number;
}

const COLORS = [
  "#FBBF24",
  "#2563EB",
  "#16A34A",
];

export default function StatusChart({
  assigned,
  inProgress,
  resolved,
}: Props) {
  const data = [
    {
      name: "Pending",
      value: assigned,
    },
    {
      name: "In Progress",
      value: inProgress,
    },
    {
      name: "Resolved",
      value: resolved,
    },
  ];

  return (
    <div className="rounded-xl border border-paper-200 bg-paper-50 p-6 shadow-sm">
      <div className="mb-6">
        <h2 className="text-xl font-semibold">
          Issue Status Distribution
        </h2>

        <p className="mt-1 text-sm text-ink-500">
          Current workload grouped by issue status.
        </p>
      </div>

      <div className="h-96">
        <ResponsiveContainer>
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              innerRadius={70}
              outerRadius={120}
              paddingAngle={3}
            >
              {data.map((_, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index]}
                />
              ))}
            </Pie>

            <Tooltip />

            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}