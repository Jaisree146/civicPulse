import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import { AxiosError } from "axios";

import ComplaintForm from "./components/ComplaintForm";
import LocationPicker from "./components/LocationPicker";

import { type ComplaintFormData } from "../validation";

import { useCreateComplaint } from "../hooks";

export default function ReportComplaint() {
  const navigate = useNavigate();

  const createComplaintMutation = useCreateComplaint();

  const [latitude, setLatitude] = useState(11.341);

  const [longitude, setLongitude] = useState(77.7172);

  const handleLocationChange = (lat: number, lng: number) => {
    setLatitude(lat);
    setLongitude(lng);
  };

  const onSubmit = async (data: ComplaintFormData) => {
    try {
      const response = await createComplaintMutation.mutateAsync({
        ...data,
        latitude,
        longitude,
      });

      toast.success(
        `Complaint ${response.complaint_number} submitted successfully.`,
      );

      setTimeout(() => {
        navigate("/citizen/complaints");
      }, 1200);
    } catch (error) {
      if (error instanceof AxiosError) {
        toast.error(
          error.response?.data?.message ?? "Failed to submit complaint.",
        );
      } else {
        toast.error("Something went wrong.");
      }
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}

      <div>
        <h1 className="text-3xl font-bold text-ink-900">Report Complaint</h1>

        <p className="mt-2 text-ink-500">
          Submit details of the civic issue along with its location.
        </p>
      </div>

      {/* Complaint Form */}

      <div className="rounded-xl border border-paper-200 bg-paper-50 p-8 shadow-sm">
        <ComplaintForm
          onSubmit={onSubmit}
          isSubmitting={createComplaintMutation.isPending}
        />
      </div>

      {/* Location */}

      <LocationPicker
        latitude={latitude}
        longitude={longitude}
        onLocationChange={handleLocationChange}
      />
    </div>
  );
}
