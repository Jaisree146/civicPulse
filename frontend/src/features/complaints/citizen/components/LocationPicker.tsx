import { useState } from "react";
import { MapPin } from "lucide-react";

import MapView from "./MapView";

interface Props {
  latitude: number;
  longitude: number;
  onLocationChange: (
    latitude: number,
    longitude: number
  ) => void;
}

export default function LocationPicker({
  latitude,
  longitude,
  onLocationChange,
}: Props) {
  const [loadingLocation, setLoadingLocation] =
    useState(false);

  const handleCurrentLocation = () => {
    if (!navigator.geolocation) {
      alert("Geolocation is not supported.");
      return;
    }

    setLoadingLocation(true);

    navigator.geolocation.getCurrentPosition(
      (position) => {
        onLocationChange(
          position.coords.latitude,
          position.coords.longitude
        );

        setLoadingLocation(false);
      },
      () => {
        alert(
          "Unable to fetch your location."
        );
        setLoadingLocation(false);
      }
    );
  };

  return (
    <div className="space-y-5 rounded-xl border border-paper-200 bg-paper-50 p-6 shadow-sm">

      <div>

        <h2 className="text-xl font-semibold text-ink-900">
          Complaint Location
        </h2>

        <p className="mt-1 text-sm text-ink-500">
          Select the location where the issue
          occurred.
        </p>

      </div>

      <MapView
        latitude={latitude}
        longitude={longitude}
        onLocationChange={onLocationChange}
      />

      <div className="grid gap-4 md:grid-cols-2">

        <div>
          <label className="auth-label">
            Latitude
          </label>

          <input
            value={latitude}
            readOnly
            className="auth-input"
          />
        </div>

        <div>
          <label className="auth-label">
            Longitude
          </label>

          <input
            value={longitude}
            readOnly
            className="auth-input"
          />
        </div>

      </div>

      <button
        type="button"
        onClick={handleCurrentLocation}
        className="auth-btn"
      >
        <MapPin size={18} />

        {loadingLocation
          ? "Fetching Location..."
          : "Use Current Location"}
      </button>

    </div>
  );
}