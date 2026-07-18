import { z } from "zod";

export const loginSchema = z.object({
    email: z.string().email("Invalid email address"),

    password: z.string().min(1,"Password is required")

});

export type LoginFormData =
    z.infer<typeof loginSchema>;

export const registerSchema = z.object({
  full_name: z
    .string()
    .min(3, "Full name is required"),

  email: z
    .string()
    .email("Invalid email address"),

  password: z
    .string()
    .min(6, "Password must be at least 8 characters"),

  phone: z
    .string()
    .regex(/^[6-9]\d{9}$/, "Invalid phone number"),
});

export type RegisterFormData =
  z.infer<typeof registerSchema>;

export const changePasswordSchema = z.object({
  old_password: z.string().min(1, "Old password is required"),
  new_password: z.string().min(6, "New password must be at least 6 characters"),
  confirm_password: z.string().min(1, "Please confirm your password"),
}).refine((data) => data.new_password === data.confirm_password, {
  message: "Passwords don't match",
  path: ["confirm_password"],
});

export type ChangePasswordFormData = z.infer<typeof changePasswordSchema>;