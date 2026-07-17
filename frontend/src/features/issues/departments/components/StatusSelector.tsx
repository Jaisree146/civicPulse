interface Props {
  value: string;
  onChange: (status: string) => void;
}

const STATUSES = [
  "Assigned",
  "In Progress",
  "Resolved",
  "Closed",
];

export default function StatusSelector({
  value,
  onChange,
}: Props) {
  return (
    <div className="space-y-2">
      <label className="text-sm font-medium text-ink-700">
        Update Status
      </label>

      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full rounded-xl border border-paper-300 bg-paper-50 px-4 py-3 outline-none transition focus:border-navy-700"
      >
        {STATUSES.map((status) => (
          <option
            key={status}
            value={status}
          >
            {status}
          </option>
        ))}
      </select>
    </div>
  );
}