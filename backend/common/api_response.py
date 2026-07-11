from flask import jsonify

class ApiResponse:
    @staticmethod
    def success(message: str,data=None,status_code: int = 200):

        response = {
            "success": True,
            "message": message,
            "data": data
        }

        return jsonify(response), status_code

    @staticmethod
    def error(message: str,status_code: int,errors=None,error_code=None):

        response = {
            "success": False,
            "message": message,
            "error_code": error_code,
            "errors": errors
        }

        return jsonify(response), status_code