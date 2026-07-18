import { Link, useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import toast from "react-hot-toast";
import { AxiosError } from "axios";
import { Mail, Lock, User, Phone, ArrowRight, Landmark } from "lucide-react";
import "./auth.css";
import { registerSchema, type RegisterFormData } from "./validation";
import { useRegister } from "./hooks";

export default function Register() {
  const navigate = useNavigate();
  const registerMutation = useRegister();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
  });

  const onSubmit = async (data: RegisterFormData) => {
    try {
      await registerMutation.mutateAsync(data);
      toast.success("Registration Successful");
      navigate("/login");
    } catch (error) {
      if (error instanceof AxiosError) {
        toast.error(error.response?.data?.message ?? "Registration Failed");
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
                Register once to file complaints, follow their progress,
                and hear directly from the department handling them.
              </p>
            </div>

            <ul className="auth-role-list">
              <li className="auth-role-item">
                <span className="auth-role-mark">01</span>
                Citizens file and track complaints
              </li>
              <li className="auth-role-item">
                <span className="auth-role-mark">02</span>
                Municipal officers assign and monitor
              </li>
              <li className="auth-role-item">
                <span className="auth-role-mark">03</span>
                Department officers resolve and close
              </li>
            </ul>

            <p className="auth-brand-bottom">Authorized access only</p>
          </aside>

          {/* Form panel */}
          <div className="auth-form-panel">
            <h2 className="auth-form-heading">Create your account</h2>
            <p className="auth-form-subheading">
              A few details, then you're in.
            </p>

            <form onSubmit={handleSubmit(onSubmit)}>
              {/* Full Name */}
              <div className="auth-field">
                <label htmlFor="reg-name" className="auth-label">
                  Full Name
                </label>
                <div className="auth-input-wrapper">
                  <User className="auth-input-icon" strokeWidth={1.75} />
                  <input
                    id="reg-name"
                    type="text"
                    placeholder="John Doe"
                    {...register("full_name")}
                    className="auth-input"
                  />
                </div>
                {errors.full_name && (
                  <p className="auth-error">{errors.full_name.message}</p>
                )}
              </div>

              {/* Email */}
              <div className="auth-field">
                <label htmlFor="reg-email" className="auth-label">
                  Email
                </label>
                <div className="auth-input-wrapper">
                  <Mail className="auth-input-icon" strokeWidth={1.75} />
                  <input
                    id="reg-email"
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

              {/* Phone */}
              <div className="auth-field">
                <label htmlFor="reg-phone" className="auth-label">
                  Phone Number
                </label>
                <div className="auth-input-wrapper">
                  <Phone className="auth-input-icon" strokeWidth={1.75} />
                  <input
                    id="reg-phone"
                    type="tel"
                    placeholder="9876543210"
                    {...register("phone")}
                    className="auth-input"
                  />
                </div>
                {errors.phone && (
                  <p className="auth-error">{errors.phone.message}</p>
                )}
              </div>

              {/* Password */}
              <div className="auth-field">
                <label htmlFor="reg-password" className="auth-label">
                  Password
                </label>
                <div className="auth-input-wrapper">
                  <Lock className="auth-input-icon" strokeWidth={1.75} />
                  <input
                    id="reg-password"
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
                disabled={registerMutation.isPending}
                className="auth-btn mt-2"
              >
                {registerMutation.isPending ? (
                  "Creating account…"
                ) : (
                  <>
                    Sign up
                    <ArrowRight className="h-4 w-4" />
                  </>
                )}
              </button>
            </form>

            <p className="auth-form-footer">
              Already have an account? <Link to="/login">Sign in</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}