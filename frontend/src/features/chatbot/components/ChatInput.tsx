import { useState } from "react";

import { SendHorizonal } from "lucide-react";

interface Props {
  onSend: (message: string) => void;

  disabled?: boolean;
}

export default function ChatInput({
  onSend,
  disabled = false,
}: Props) {

  const [message, setMessage] =
    useState("");

  function handleSubmit() {

    const trimmed = message.trim();

    if (!trimmed) return;

    onSend(trimmed);

    setMessage("");

  }

  return (

    <div className="border-t border-paper-200 bg-white p-4">

      <div className="flex items-end gap-3">

        <textarea
          value={message}
          rows={2}
          disabled={disabled}
          placeholder="Ask about complaint status or municipal policies..."
          onChange={(e) =>
            setMessage(e.target.value)
          }
          onKeyDown={(e) => {

            if (
              e.key === "Enter" &&
              !e.shiftKey
            ) {

              e.preventDefault();

              handleSubmit();

            }

          }}
          className="flex-1 resize-none rounded-xl border border-paper-300 bg-paper-50 px-4 py-3 outline-none transition focus:border-navy-600"
        />

        <button
          disabled={
            disabled ||
            message.trim() === ""
          }
          onClick={handleSubmit}
          className="rounded-xl bg-navy-800 p-3 text-white transition hover:bg-navy-700 disabled:cursor-not-allowed disabled:opacity-50"
        >

          <SendHorizonal size={20} />

        </button>

      </div>

    </div>

  );

}