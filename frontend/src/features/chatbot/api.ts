import api from "../../api/axios";
import { API_ENDPOINTS } from "../../api/endpoints";

import type { ChatRequest, ChatResponse } from "./types";

export const chatApi = {
  sendMessage: async (data: ChatRequest): Promise<ChatResponse> => {
    const response = await api.post(API_ENDPOINTS.CHAT.CHAT, data);

    return response.data.data;
  },
};
