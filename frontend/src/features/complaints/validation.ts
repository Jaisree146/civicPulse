import { z } from "zod";

export const complaintSchema = z.object({
  title: z
    .string()
    .min(5, "Title must contain at least 5 characters")
    .max(100),

  description: z
    .string()
    .min(
      15,
      "Description must contain at least 15 characters"
    )
    .max(1000),
});

export type ComplaintFormData =
  z.infer<typeof complaintSchema>;