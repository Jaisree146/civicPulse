import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { FileText, AlignLeft, ArrowRight } from "lucide-react";

import {
  complaintSchema,
  type ComplaintFormData,
} from "../../validation";

interface Props {
  onSubmit: (data: ComplaintFormData) => void;
  isSubmitting: boolean;
}

export default function ComplaintForm({
  onSubmit,
  isSubmitting,
}: Props) {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ComplaintFormData>({
    resolver: zodResolver(complaintSchema),
  });

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-8"
    >
      {/* Title */}

      <div className="auth-field">
        <label className="auth-label">
          Complaint Title
        </label>

        <div className="auth-input-wrapper">
          <FileText
            className="auth-input-icon"
            strokeWidth={1.75}
          />

          <input
            type="text"
            placeholder="Enter complaint title"
            {...register("title")}
            className="auth-input"
          />
        </div>

        {errors.title && (
          <p className="auth-error">
            {errors.title.message}
          </p>
        )}
      </div>

      {/* Description */}

      <div className="auth-field">
        <label className="auth-label">
          Description
        </label>

        <div className="relative">
          <AlignLeft
            className="absolute left-4 top-4 text-ink-400"
            size={18}
          />

          <textarea
            rows={6}
            placeholder="Describe the issue in detail..."
            {...register("description")}
            className="w-full rounded-xl border border-paper-300 bg-paper-50 py-3 pl-12 pr-4 text-ink-900 outline-none transition focus:border-navy-500 focus:ring-2 focus:ring-navy-100"
          />
        </div>

        {errors.description && (
          <p className="auth-error">
            {errors.description.message}
          </p>
        )}
      </div>

      {/* Submit */}

      <div className="flex justify-end">
        <button
          type="submit"
          disabled={isSubmitting}
          className="auth-btn"
        >
          {isSubmitting ? (
            "Submitting..."
          ) : (
            <>
              Submit Complaint

              <ArrowRight
                size={18}
              />
            </>
          )}
        </button>
      </div>
    </form>
  );
}