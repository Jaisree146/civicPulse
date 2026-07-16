import { useParams } from "react-router-dom";

import ComplaintInfo from "./components/ComplaintInfo";

import { useComplaintDetails } from "../hooks";

export default function ComplaintDetails() {
  const { complaintNumber } =
    useParams();

  const {
    data,
    isLoading,
    isError,
  } = useComplaintDetails(
    complaintNumber ?? ""
  );

  if (isLoading) {
    return (
      <div className="flex h-full items-center justify-center">
        Loading complaint...
      </div>
    );
  }

  if (isError || !data) {
    return (
      <div className="flex h-full items-center justify-center text-red-500">
        Complaint not found.
      </div>
    );
  }

  return (
    <div className="space-y-8">

      <div>

        <h1 className="text-3xl font-bold text-ink-900">
          Complaint Details
        </h1>

        <p className="mt-2 text-ink-500">
          View complete information about your complaint.
        </p>

      </div>

      <ComplaintInfo
        complaint={data}
      />

    </div>
  );
}