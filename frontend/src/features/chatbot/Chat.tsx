import { useEffect, useRef, useState } from "react";
import { AxiosError } from "axios";
import toast from "react-hot-toast";

import { useChat } from "./hooks";

import ChatBubble from "./components/ChatBubble";
import ChatInput from "./components/ChatInput";

import type { ChatMessage } from "./types";

export default function Chat() {

  const chatMutation = useChat();

  const bottomRef = useRef<HTMLDivElement>(null);

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: crypto.randomUUID(),
      sender: "assistant",
      text:
        "Hello! 👋 I can help you with complaint status and municipal policy questions.",
      createdAt: new Date(),
    },
  ]);

  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });

  }, [messages]);

  async function handleSend(
    message: string
  ) {

    const userMessage: ChatMessage = {

      id: crypto.randomUUID(),

      sender: "user",

      text: message,

      createdAt: new Date(),

    };

    setMessages((previous) => [
      ...previous,
      userMessage,
    ]);

    try {

      const response =
        await chatMutation.mutateAsync({
          message,
        });

      const assistantMessage: ChatMessage = {

        id: crypto.randomUUID(),

        sender: "assistant",

        text: response,

        createdAt: new Date(),

      };

      setMessages((previous) => [
        ...previous,
        assistantMessage,
      ]);

    } catch (error) {

      if (error instanceof AxiosError) {

        toast.error(
          error.response?.data?.message ??
            "Unable to get response."
        );

      } else {

        toast.error(
          "Something went wrong."
        );

      }

    }

  }

  return (

    <div className="flex h-[80vh] flex-col rounded-xl border border-paper-200 bg-paper-50 shadow-sm">

      {/* Header */}

      <div className="border-b border-paper-200 p-5">

        <h1 className="font-serif text-2xl font-bold text-ink-900">
          CivicPulse Assistant
        </h1>

        <p className="mt-1 text-sm text-ink-500">
          Ask about your complaint status or municipal policies.
        </p>

      </div>

      {/* Suggested Questions */}

      <div className="flex flex-wrap gap-3 border-b border-paper-200 p-4">

        <button
          onClick={() =>
            handleSend(
              "What is the status of my complaint?"
            )
          }
          className="rounded-full border border-paper-300 bg-paper-50 px-4 py-2 text-sm transition hover:bg-paper-100"
        >
          Complaint Status
        </button>

        <button
          onClick={() =>
            handleSend(
              "What is the resolution time for road damage?"
            )
          }
          className="rounded-full border border-paper-300 bg-paper-50 px-4 py-2 text-sm transition hover:bg-paper-100"
        >
          Policy Details
        </button>

      </div>

      {/* Messages */}

      <div className="flex-1 space-y-4 overflow-y-auto p-5">

        {messages.map((message) => (

          <ChatBubble

            key={message.id}

            message={message}

          />

        ))}

        {chatMutation.isPending && (

          <div className="text-sm italic text-ink-500">
            Assistant is typing...
          </div>

        )}

        <div ref={bottomRef} />

      </div>

      {/* Input */}

      <ChatInput

        onSend={handleSend}

        disabled={chatMutation.isPending}

      />

    </div>

  );

}