import { Building2 } from "lucide-react";

import type { Department } from "../../types";

interface Props {
  departments: Department[];
  selectedDepartment: number | "";
  onChange: (departmentId: number) => void;
}

export default function DepartmentSelector({
  departments,
  selectedDepartment,
  onChange,
}: Props) {
  return (
    <div className="space-y-2">

      <label className="flex items-center gap-2 text-sm font-medium text-ink-700">
        <Building2 size={18} />
        Assign Department
      </label>

      <select
        value={selectedDepartment}
        onChange={(e) =>
          onChange(Number(e.target.value))
        }
        className="w-full rounded-xl border border-paper-300 bg-paper-50 px-4 py-3 outline-none transition focus:border-navy-600"
      >
        <option value="">
          Select Department
        </option>

        {departments.map((department) => (
          <option
            key={department.id}
            value={department.id}
          >
            {department.department_name}
          </option>
        ))}
      </select>

    </div>
  );
}