import { Building2 } from "lucide-react";

import { useDepartments } from "../hooks";

import DepartmentCard from "./components/DepartmentCard";

export default function Departments() {

  const {
    data: departments,
    isLoading,
    isError,
  } = useDepartments();

  if (isLoading) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        Loading departments...
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex h-[70vh] items-center justify-center text-red-600">
        Failed to load departments.
      </div>
    );
  }

  return (

    <div className="space-y-8">

      <div>

        <h1 className="font-serif text-3xl font-bold text-ink-900">
          Departments
        </h1>

        <p className="mt-2 text-ink-500">
          Select a department to view its assigned issues.
        </p>

      </div>

      {departments && departments.length === 0 && (

        <div className="rounded-xl border border-dashed border-paper-300 bg-paper-50 px-8 py-20 text-center">

          <Building2
            size={60}
            className="mx-auto text-ink-300"
          />

          <h2 className="mt-6 text-2xl font-semibold text-ink-900">
            No Departments
          </h2>

        </div>

      )}

      {departments && departments.length > 0 && (

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">

          {departments.map((department) => (

            <DepartmentCard

              key={department.id}

              department={department}

            />

          ))}

        </div>

      )}

    </div>

  );
}