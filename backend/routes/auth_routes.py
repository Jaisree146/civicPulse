from flask import Blueprint

from controllers.auth_controller import AuthController

auth_bp = Blueprint("auth",__name__,url_prefix="/api/auth")
auth_bp.post("/register")(AuthController.register)
auth_bp.post("/login")(AuthController.login)
auth_bp.post("/refresh")(AuthController.refresh_token)
auth_bp.post("/logout")(AuthController.logout)
auth_bp.route("/change-password",methods=["PUT"])(AuthController.change_password)