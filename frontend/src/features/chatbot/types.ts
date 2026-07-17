export interface ChatRequest {
  message: string;
}

export type ChatResponse = string;

export interface ChatMessage {
  id: string;

  sender: "user" | "assistant";

  text: string;

  createdAt: Date;
}