from datetime import datetime, timedelta, timezone

import jwt

from config.settings import Settings
from exceptions.auth_exceptions import (
    InvalidAccessTokenException,
    InvalidRefreshTokenException,
)


class JWTHandler:
    @staticmethod
    def generate_access_token(user_id: int, role: str) -> str:
        payload = {
            "user_id": user_id,
            "role": role,
            "type": "access",
            "exp": datetime.utcnow()
            + timedelta(minutes=Settings.JWT_ACCESS_TOKEN_EXPIRY_MINUTES),
        }
        return jwt.encode(
            payload,
            Settings.JWT_ACCESS_SECRET_KEY,
            algorithm="HS256",
        )

    @staticmethod
    def generate_refresh_token(user_id: int) -> str:
        payload = {
            "user_id": user_id,
            "type": "refresh",
            "exp": datetime.utcnow()
            + timedelta(days=Settings.JWT_REFRESH_TOKEN_EXPIRY_DAYS),
        }

        return jwt.encode(
            payload,
            Settings.JWT_REFRESH_SECRET_KEY,
            algorithm="HS256",
        )

    @staticmethod
    def decode_access_token(token: str) -> dict:
        """Decode and validate an access token."""
        try:
            return jwt.decode(
                token,
                Settings.JWT_ACCESS_SECRET_KEY,
                algorithms=["HS256"],
            )
        except jwt.ExpiredSignatureError as exc:
            raise InvalidAccessTokenException() from exc
        except jwt.InvalidTokenError as exc:
            raise InvalidAccessTokenException() from exc

    @staticmethod
    def decode_refresh_token(token: str) -> dict:
        """Decode and validate a refresh token."""
        try:
            return jwt.decode(
                token,
                Settings.JWT_REFRESH_SECRET_KEY,
                algorithms=["HS256"],
            )
        except jwt.ExpiredSignatureError as exc:
            raise InvalidRefreshTokenException() from exc
        except jwt.InvalidTokenError as exc:
            raise InvalidRefreshTokenException() from exc