export const PRIORITY_STYLES: Record<
  string,
  {
    bg: string;
    text: string;
    border: string;
  }
> = {
  Low: {
    bg: "bg-green-50",
    text: "text-green-700",
    border: "border-green-200",
  },

  Medium: {
    bg: "bg-yellow-50",
    text: "text-yellow-700",
    border: "border-yellow-200",
  },

  High: {
    bg: "bg-orange-50",
    text: "text-orange-700",
    border: "border-orange-200",
  },

  Critical: {
    bg: "bg-red-50",
    text: "text-red-700",
    border: "border-red-200",
  },
};

export const STATUS_STYLES: Record<
  string,
  {
    bg: string;
    text: string;
    border: string;
    dot: string;
  }
> = {
  "Pending Review": {
    bg: "bg-yellow-50",
    text: "text-yellow-700",
    border: "border-yellow-200",
    dot: "bg-yellow-500",
  },

  Assigned: {
    bg: "bg-indigo-50",
    text: "text-indigo-700",
    border: "border-indigo-200",
    dot: "bg-indigo-500",
  },

  "In Progress": {
    bg: "bg-blue-50",
    text: "text-blue-700",
    border: "border-blue-200",
    dot: "bg-blue-500",
  },

  Resolved: {
    bg: "bg-green-50",
    text: "text-green-700",
    border: "border-green-200",
    dot: "bg-green-500",
  },
};

export const DEFAULT_STYLE = {
  bg: "bg-paper-100",
  text: "text-ink-600",
  border: "border-paper-300",
  dot: "bg-ink-400",
};