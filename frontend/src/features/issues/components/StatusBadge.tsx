import {
  DEFAULT_STYLE,
  STATUS_STYLES,
} from "../constants";

interface Props {
  status: string;
}

export default function StatusBadge({
  status,
}: Props) {
  const style =
    STATUS_STYLES[status] ??
    DEFAULT_STYLE;

  return (
    <span
      className={`inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-semibold ${style.bg} ${style.text} ${style.border}`}
    >
      <span
        className={`h-2 w-2 rounded-full ${style.dot}`}
      />

      {status}
    </span>
  );
}