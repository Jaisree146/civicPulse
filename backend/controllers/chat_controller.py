from flask import request, g

from common.api_response import ApiResponse

from services.chat_service import ChatService


class ChatController:

    @staticmethod
    def chat():

        current_user = g.current_user

        data = request.get_json()

        message = data.get("message")

        if not message:

            return ApiResponse.error(

                message="Message is required.",

                status_code=400

            )

        response = ChatService.chat(

            current_user=current_user,

            message=message

        )

        return ApiResponse.success(

            message="Chat response generated successfully.",

            data=response

        )