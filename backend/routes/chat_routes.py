from flask import Blueprint

from controllers.chat_controller import ChatController

from middleware.auth_middleware import token_required


chat_bp = Blueprint("chat",__name__,url_prefix="/api/chat")


@chat_bp.route(

    "",

    methods=["POST"]

)

@token_required
def chat():

    return ChatController.chat()