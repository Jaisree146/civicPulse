import { useMutation } from "@tanstack/react-query";

import { chatApi } from "./api";

export function useChat() {

  return useMutation({

    mutationFn: chatApi.sendMessage,

  });

}