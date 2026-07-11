from functools import wraps

from flask import g, request

from exceptions.auth_exceptions import InvalidAccessTokenException
from repositories.user_repository import UserRepository
from utils.jwt_handler import JWTHandler


def token_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if (
            auth_header is None
            or not auth_header.startswith("Bearer ")
        ):
            raise InvalidAccessTokenException()

        token = auth_header.split(" ")[1]

        payload = JWTHandler.decode_access_token(token)

        user = UserRepository.get_by_id(
            payload["user_id"]
        )

        if user is None:
            raise InvalidAccessTokenException()

        g.current_user = user

        return func(*args, **kwargs)

    return wrapper