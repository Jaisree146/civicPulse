import { Link, useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import toast from "react-hot-toast";
import { AxiosError } from "axios";
import { Lock, KeyRound, ArrowRight, Landmark } from "lucide-react";
import "./auth.css";
import { changePasswordSchema, type ChangePasswordFormData } from "./validation";
import { useChangePassword } from "./hooks";

export default function ChangePassword() {
  const navigate = useNavigate();
  const changePasswordMutation = useChangePassword();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<ChangePasswordFormData>({
    resolver: zodResolver(changePasswordSchema),
  });

  const onSubmit = async (data: ChangePasswordFormData) => {
    try {
      await changePasswordMutation.mutateAsync(data);
      toast.success("Password changed successfully");
      reset();
      navigate("/login");
    } catch (error) {
      if (error instanceof AxiosError) {
        toast.error(
          error.response?.data?.message ?? "Failed to change password"
        );
      } else {
        toast.error("Something went wrong");
      }
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-solo-container auth-animate">
        <div className="auth-solo-panel">
          {/* Header */}
          <div className="auth-solo-header">
            <div className="auth-solo-seal">
              <Landmark className="h-5 w-5" strokeWidth={1.75} />
            </div>
            <p className="auth-solo-eyebrow">Security</p>
            <h1 className="auth-solo-title">Change Password</h1>
            <p className="auth-solo-subtitle">
              Update your password to stay secure
            </p>
          </div>

          <form onSubmit={handleSubmit(onSubmit)}>
            {/* Current Password */}
            <div className="auth-field">
              <label htmlFor="cp-old" className="auth-label">
                Current Password
              </label>
              <div className="auth-input-wrapper">
                <Lock className="auth-input-icon" strokeWidth={1.75} />
                <input
                  id="cp-old"
                  type="password"
                  placeholder="••••••••"
                  {...register("old_password")}
                  className="auth-input"
                />
              </div>
              {errors.old_password && (
                <p className="auth-error">{errors.old_password.message}</p>
              )}
            </div>

            {/* New Password */}
            <div className="auth-field">
              <label htmlFor="cp-new" className="auth-label">
                New Password
              </label>
              <div className="auth-input-wrapper">
                <KeyRound className="auth-input-icon" strokeWidth={1.75} />
                <input
                  id="cp-new"
                  type="password"
                  placeholder="••••••••"
                  {...register("new_password")}
                  className="auth-input"
                />
              </div>
              {errors.new_password && (
                <p className="auth-error">{errors.new_password.message}</p>
              )}
            </div>

            {/* Confirm Password */}
            <div className="auth-field">
              <label htmlFor="cp-confirm" className="auth-label">
                Confirm Password
              </label>
              <div className="auth-input-wrapper">
                <KeyRound className="auth-input-icon" strokeWidth={1.75} />
                <input
                  id="cp-confirm"
                  type="password"
                  placeholder="••••••••"
                  {...register("confirm_password")}
                  className="auth-input"
                />
              </div>
              {errors.confirm_password && (
                <p className="auth-error">{errors.confirm_password.message}</p>
              )}
            </div>

            {/* Submit */}
            <button
              type="submit"
              disabled={changePasswordMutation.isPending}
              className="auth-btn mt-4"
            >
              {changePasswordMutation.isPending ? (
                "Updating…"
              ) : (
                <>
                  Update Password
                  <ArrowRight className="h-4 w-4" />
                </>
              )}
            </button>
          </form>

          {/* Footer */}
          <div className="auth-solo-footer">
            <Link to="/login">
              ← Back to login
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
