from flask import request

from middleware.auth_middleware import token_required
from common.api_response import ApiResponse
from exceptions.auth_exceptions import RefreshTokenMissingException
from services.auth_service import AuthService
from validators.auth_validator import AuthValidator
from flask import g

class AuthController:

    @staticmethod
    def register():

        data = request.get_json()

        AuthValidator.validate_register(data)

        user = AuthService.register(
            full_name=data["full_name"],
            email=data["email"],
            password=data["password"],
            phone=data["phone"]
        )

        return ApiResponse.success(
            message="User registered successfully.",
            data={
                "user_id": user.id
            },
            status_code=201
        )

    @staticmethod
    def login():

        data = request.get_json()

        AuthValidator.validate_login(data)

        tokens = AuthService.login(
            email=data["email"],
            password=data["password"]
        )

        response, status_code = ApiResponse.success(
            message="Login successful.",
            data={
            "access_token": tokens["access_token"],
            "user": tokens["user"]
            },
            status_code=200
        )

        response.set_cookie(
            "refresh_token",
            tokens["refresh_token"],
            httponly=True,
            secure=False,          # True in production
            samesite="Lax",
            max_age=7 * 24 * 60 * 60
        )

        return response, status_code

    @staticmethod
    def refresh_token():

        refresh_token = request.cookies.get(
            "refresh_token"
        )

        if refresh_token is None:
            raise RefreshTokenMissingException()

        token = AuthService.refresh_access_token(
            refresh_token
        )

        return ApiResponse.success(
            message="Access token refreshed successfully.",
            data={
                "access_token": token["access_token"],
                "user":token["user"]
            },
            status_code=200
        )

    @staticmethod
    def logout():

        refresh_token = request.cookies.get(
            "refresh_token"
        )

        if refresh_token is None:
            raise RefreshTokenMissingException()

        AuthService.logout(refresh_token)

        response, status_code = ApiResponse.success(
            message="Logout successful.",
            status_code=200
        )

        response.delete_cookie(
            "refresh_token"
        )

        return response, status_code
    
    @staticmethod
    @token_required
    def change_password():

        data = request.get_json()

        AuthValidator.validate_change_password(data)

        AuthService.change_password(
            user_id=g.current_user.id,
            old_password=data["old_password"],
            new_password=data["new_password"]
        )

        return ApiResponse.success(
            message="Password changed successfully.",
            status_code=200
        )