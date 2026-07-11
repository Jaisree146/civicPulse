from datetime import datetime, timedelta

from common.constants import Roles
from common.logger import logger
from exceptions.auth_exceptions import (
    InvalidCredentialsException,
    InvalidRefreshTokenException,
    RefreshTokenRevokedException,
    RoleNotFoundException,
    UserAlreadyExistsException,
    InvalidOldPasswordException
)
from models.refresh_token import RefreshToken
from models.user import User
from repositories.refresh_token_repository import RefreshTokenRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from utils.jwt_handler import JWTHandler
from utils.password import PasswordManager
from utils.token_hash import TokenHashManager


class AuthService:

    @staticmethod
    def register(full_name: str, email: str, password: str, phone: str) -> User:

        existing_user = UserRepository.get_by_email(email)

        if existing_user:
            logger.warning(
                "Registration failed. Email already exists: %s",
                email
            )
            raise UserAlreadyExistsException()

        citizen_role = RoleRepository.get_by_name(
            Roles.CITIZEN
        )

        if citizen_role is None:
            logger.error(
                "Citizen role not found."
            )
            raise RoleNotFoundException()

        password_hash = PasswordManager.hash_password(
            password
        )

        user = User(
            full_name=full_name,
            email=email,
            password_hash=password_hash,
            phone=phone,
            role_id=citizen_role.id,
            department_id=None
        )

        created_user = UserRepository.create(user)

        logger.info(
            "User registered successfully. User ID: %s",
            created_user.id
        )

        return created_user

    @staticmethod
    def login(email: str, password: str) -> dict:

        user = UserRepository.get_by_email(email)

        if user is None:
            logger.warning(
                "Login failed. User not found: %s",
                email
            )
            raise InvalidCredentialsException()

        if not PasswordManager.verify_password(
            password,
            user.password_hash
        ):
            logger.warning(
                "Login failed. Invalid password for: %s",
                email
            )
            raise InvalidCredentialsException()

        existing_token = (
            RefreshTokenRepository.get_active_token_by_user_id(
                user.id
            )
        )

        if existing_token:
            RefreshTokenRepository.revoke(
                existing_token
            )

        access_token = JWTHandler.generate_access_token(
            user.id,
            user.role.role_name
        )

        refresh_token = JWTHandler.generate_refresh_token(
            user.id
        )

        refresh_token_hash = TokenHashManager.hash_token(
            refresh_token
        )

        refresh_token_obj = RefreshToken(
            user_id=user.id,
            token_hash=refresh_token_hash,
            expires_at=datetime.utcnow() + timedelta(days=7)
        )

        RefreshTokenRepository.create(
            refresh_token_obj
        )

        logger.info(
            "User logged in successfully. User ID: %s",
            user.id
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    @staticmethod
    def refresh_access_token(refresh_token: str) -> dict:

        payload = JWTHandler.decode_refresh_token(
            refresh_token
        )

        refresh_token_hash = TokenHashManager.hash_token(
            refresh_token
        )

        stored_token = (
            RefreshTokenRepository.get_by_token_hash(
                refresh_token_hash
            )
        )

        if stored_token is None:
            logger.warning(
                "Refresh failed. Token not found."
            )
            raise InvalidRefreshTokenException()

        if stored_token.is_revoked:
            logger.warning(
                "Refresh failed. Token revoked."
            )
            raise RefreshTokenRevokedException()

        if stored_token.expires_at < datetime.utcnow():
            RefreshTokenRepository.revoke(
                stored_token
            )
            logger.warning(
                "Refresh failed. Token expired."
            )
            raise InvalidRefreshTokenException()

        user = UserRepository.get_by_id(
            payload["user_id"]
        )

        if user is None:
            logger.warning(
                "Refresh failed. User not found."
            )
            raise InvalidRefreshTokenException()

        access_token = JWTHandler.generate_access_token(
            user.id,
            user.role.role_name
        )

        logger.info(
            "Access token refreshed. User ID: %s",
            user.id
        )

        return {
            "access_token": access_token
        }

    @staticmethod
    def logout(refresh_token: str) -> None:

        refresh_token_hash = TokenHashManager.hash_token(
            refresh_token
        )

        stored_token = (
            RefreshTokenRepository.get_by_token_hash(
                refresh_token_hash
            )
        )

        if stored_token is None:
            logger.warning(
                "Logout failed. Refresh token not found."
            )
            raise InvalidRefreshTokenException()

        RefreshTokenRepository.revoke(
            stored_token
        )

        logger.info(
            "User logged out successfully. User ID: %s",
            stored_token.user_id
        )
    @staticmethod
    def change_password(
    user_id: int,
    old_password: str,
    new_password: str
    ):

        user = UserRepository.get_by_id(user_id)

        if user is None:
            raise InvalidCredentialsException()

        if not PasswordManager.verify_password(old_password,user.password_hash):
            raise InvalidOldPasswordException()

        user.password_hash = (PasswordManager.hash_password(new_password))

        UserRepository.update(user)

        active_token = (RefreshTokenRepository.get_active_token_by_user_id(user.id))

        if active_token:
            RefreshTokenRepository.revoke(active_token)
        logger.info(
            "Password changed successfully. User ID=%s",
            user.id
        )