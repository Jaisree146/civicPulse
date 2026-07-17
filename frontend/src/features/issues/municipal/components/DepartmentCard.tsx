import { ArrowRight, Building2 } from "lucide-react";
import { useNavigate } from "react-router-dom";

import type { Department } from "../../types";

interface Props {
  department: Department;
}

export default function DepartmentCard({
  department,
}: Props) {

  const navigate = useNavigate();

  return (

    <div className="rounded-xl border border-paper-200 bg-paper-50 p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">

      <div className="flex items-center gap-4">

        <div className="rounded-xl bg-navy-100 p-3">

          <Building2
            size={26}
            className="text-navy-700"
          />

        </div>

        <div>

          <h2 className="text-lg font-semibold text-ink-900">
            {department.department_name}
          </h2>

          {department.description && (
            <p className="mt-1 text-sm text-ink-500">
              {department.description}
            </p>
          )}

        </div>

      </div>

      <div className="mt-6 border-t border-paper-200 pt-5">

        <button
          onClick={() =>
            navigate(
              `/municipal/departments/${department.id}`
            )
          }
          className="flex items-center gap-2 font-medium text-navy-800 transition hover:text-gold-600"
        >
          View Issues

          <ArrowRight size={18} />

        </button>

      </div>

    </div>

  );
}