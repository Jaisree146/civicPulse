from functools import wraps

from flask import g

from common.constants import Roles
from exceptions.auth_exceptions import AuthenticationException


def roles_required(*allowed_roles):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            user_role = g.current_user.role.role_name

            if user_role not in allowed_roles:
                raise AuthenticationException(
                    message="You are not authorized to perform this action.",
                    status_code=403,
                    error_code="AUTH_010"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator