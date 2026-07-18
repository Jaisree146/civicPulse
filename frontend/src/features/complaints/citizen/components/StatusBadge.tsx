interface Props {
  status: string;
}
import {
  COMPLAINT_STATUS_STYLES,
  DEFAULT_STATUS_STYLE,
} from "../../constants";
export default function StatusBadge({
  status,
}: Props) {
  const style =
  COMPLAINT_STATUS_STYLES[
    status
  ] ?? DEFAULT_STATUS_STYLE;
  return (
    <span
      className={`inline-flex items-center gap-2 rounded-full border px-3 py-1 text-sm font-semibold ${style.bg} ${style.border} ${style.text}`}
    >
      <span
        className={`h-2 w-2 rounded-full ${style.dot}`}
      />
      {status}
    </span>
  );
}