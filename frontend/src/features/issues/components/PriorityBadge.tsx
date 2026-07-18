import {
  DEFAULT_STYLE,
  PRIORITY_STYLES,
} from "../constants";

interface Props {
  priority: string;
}

export default function PriorityBadge({
  priority,
}: Props) {
  const style =
    PRIORITY_STYLES[priority] ??
    DEFAULT_STYLE;

  return (
    <span
      className={`rounded-full border px-3 py-1 text-xs font-semibold ${style.bg} ${style.text} ${style.border}`}
    >
      {priority}
    </span>
  );
}