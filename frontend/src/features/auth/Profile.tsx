import { useNavigate } from "react-router-dom";
import { User, Shield, KeyRound, ChevronRight } from "lucide-react";

import { useAuth } from "../../hooks/useAuth";

export default function Profile() {
  const { user } = useAuth();
  const navigate = useNavigate();

  return (
    <div className="mx-auto max-w-3xl space-y-8">

      {/* Profile Information */}
      <div className="rounded-xl border bg-white p-6 shadow-sm">
        <h1 className="mb-6 text-2xl font-bold text-gray-900">
          My Profile
        </h1>

        <div className="space-y-5">

          <div className="flex items-center gap-4">
            <User className="h-5 w-5 text-blue-600" />
            <div>
              <p className="text-sm text-gray-500">Name</p>
              <p className="font-medium text-gray-900">{user?.full_name}</p>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <Shield className="h-5 w-5 text-green-600" />
            <div>
              <p className="text-sm text-gray-500">Role</p>
              <p className="font-medium text-gray-900">{user?.role}</p>
            </div>
          </div>


        </div>
      </div>

      {/* Change Password trigger */}
      <div className="rounded-xl border bg-white p-6 shadow-sm">
        <button
          type="button"
          onClick={() => navigate("/change-password")}
          className="flex w-full items-center justify-between rounded-lg border border-gray-200 px-4 py-3 text-left transition hover:bg-gray-50"
        >
          <div className="flex items-center gap-3">
            <KeyRound className="h-5 w-5 text-blue-600" />
            <div>
              <p className="font-medium text-gray-900">Change Password</p>
              <p className="text-sm text-gray-500">
                Update your password to keep your account secure
              </p>
            </div>
          </div>
          <ChevronRight className="h-5 w-5 text-gray-400" />
        </button>
      </div>

    </div>
  );
}