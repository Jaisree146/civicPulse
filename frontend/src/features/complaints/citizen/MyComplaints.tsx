import ComplaintItem from "./components/ComplaintItem";
import EmptyComplaints from "./components/EmptyComplaints";

import { useMyComplaints } from "../hooks";

export default function MyComplaints() {
  const {
    data,
    isLoading,
    isError,
  } = useMyComplaints();

  if (isLoading) {
    return (
      <div className="flex h-full items-center justify-center">
        Loading complaints...
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex h-full items-center justify-center text-red-500">
        Failed to load complaints.
      </div>
    );
  }

  return (
    <div className="space-y-8">

      <div>

        <h1 className="text-3xl font-bold text-ink-900">
          My Complaints
        </h1>

        <p className="mt-2 text-ink-500">
          Track every complaint you've
          submitted to the municipality.
        </p>

      </div>

      {!data || data.length === 0 ? (
        <EmptyComplaints />
      ) : (
        <div className="grid gap-6 lg:grid-cols-2">
          {data.map((complaint) => (
            <ComplaintItem
              key={complaint.complaint_number}
              complaint={complaint}
            />
          ))}
        </div>
      )}

    </div>
  );
}