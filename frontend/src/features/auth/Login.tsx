import { Link, useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import toast from "react-hot-toast";
import { AxiosError } from "axios";
import { Mail, Lock, ArrowRight, Landmark } from "lucide-react";
import "./auth.css";
import { loginSchema, type LoginFormData } from "./validation";
import { useLogin } from "./hooks";
import { useAuth } from "../../hooks/useAuth";

export default function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const loginMutation = useLogin();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginFormData) => {
    try {
      const response = await loginMutation.mutateAsync(data);
      login(response.access_token, response.user);
      toast.success("Login Successful");

      switch (response.user.role) {
        case "Citizen":
          navigate("/citizen/dashboard");
          break;
        case "Municipal Officer":
          navigate("/municipal/dashboard");
          break;
        case "Department Officer":
          navigate("/department/dashboard");
          break;
        default:
          navigate("/");
      }
    } catch (error) {
      if (error instanceof AxiosError) {
        toast.error(error.response?.data?.message ?? "Login Failed");
      } else {
        toast.error("Something went wrong");
      }
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-container auth-animate">
        <div className="auth-shell">
          {/* Authority panel */}
          <aside className="auth-brand-panel">
            <div className="auth-brand-top">
              <div className="auth-seal">
                <Landmark className="h-5 w-5" strokeWidth={1.75} />
              </div>
              <p className="auth-eyebrow">Civic Grievance Portal</p>
              <h1 className="auth-brand-title">CivicPulse</h1>
              <div className="auth-brand-rule" />
              <p className="auth-brand-copy">
                A shared record between residents and municipal departments —
                every complaint logged, routed, and tracked to resolution.
              </p>
            </div>

            <ul className="auth-role-list">
              <li className="auth-role-item">
                <span className="auth-role-mark">01</span>
                Secure digital access
              </li>

              <li className="auth-role-item">
                <span className="auth-role-mark">02</span>
                Verified role-based permissions
              </li>

              <li className="auth-role-item">
                <span className="auth-role-mark">03</span>
                Reliable municipal collaboration
              </li>
            </ul>

            <p className="auth-brand-bottom">Authorized access only</p>
          </aside>

          {/* Form panel */}
          <div className="auth-form-panel">
            <h2 className="auth-form-heading">Sign in</h2>
            <p className="auth-form-subheading">
              Enter your credentials to reach your dashboard.
            </p>

            <form onSubmit={handleSubmit(onSubmit)}>
              {/* Email */}
              <div className="auth-field">
                <label htmlFor="login-email" className="auth-label">
                  Email
                </label>
                <div className="auth-input-wrapper">
                  <Mail className="auth-input-icon" strokeWidth={1.75} />
                  <input
                    id="login-email"
                    type="email"
                    placeholder="you@example.com"
                    {...register("email")}
                    className="auth-input"
                  />
                </div>
                {errors.email && (
                  <p className="auth-error">{errors.email.message}</p>
                )}
              </div>

              {/* Password */}
              <div className="auth-field">
                <div className="auth-label-row">
                  <label htmlFor="login-password" className="auth-label">
                    Password
                  </label>
                </div>
                <div className="auth-input-wrapper">
                  <Lock className="auth-input-icon" strokeWidth={1.75} />
                  <input
                    id="login-password"
                    type="password"
                    placeholder="••••••••"
                    {...register("password")}
                    className="auth-input"
                  />
                </div>
                {errors.password && (
                  <p className="auth-error">{errors.password.message}</p>
                )}
              </div>

              {/* Submit */}
              <button
                type="submit"
                disabled={loginMutation.isPending}
                className="auth-btn mt-2"
              >
                {loginMutation.isPending ? (
                  "Signing in…"
                ) : (
                  <>
                    Sign in
                    <ArrowRight className="h-4 w-4" />
                  </>
                )}
              </button>
            </form>

            <p className="auth-form-footer">
              Don't have an account? <Link to="/register">Sign up</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
