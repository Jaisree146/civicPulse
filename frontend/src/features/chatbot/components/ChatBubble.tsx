import clsx from "clsx";

import type { ChatMessage } from "../types";

interface Props {
  message: ChatMessage;
}

export default function ChatBubble({
  message,
}: Props) {

  const isUser =
    message.sender === "user";

  return (

    <div
      className={clsx(
        "flex",
        isUser
          ? "justify-end"
          : "justify-start"
      )}
    >

      <div
        className={clsx(
          "max-w-[80%] rounded-2xl px-4 py-3 shadow-sm",

          isUser
            ? "bg-navy-800 text-white rounded-br-md"
            : "bg-paper-100 border border-paper-300 text-ink-900 rounded-bl-md"
        )}
      >

        <p className="whitespace-pre-wrap break-words text-sm leading-6">
          {message.text}
        </p>

        <p
          className={clsx(
            "mt-2 text-right text-[10px]",

            isUser
              ? "text-paper-200"
              : "text-ink-400"
          )}
        >
          {message.createdAt.toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })}
        </p>

      </div>

    </div>

  );

}