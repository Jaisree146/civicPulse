class AppException(Exception):

    def __init__(self,message: str = "Something went wrong.",status_code: int = 400,error_code: str = "APP_001"):

        self.message = message
        self.status_code = status_code
        self.error_code = error_code

        super().__init__(self.message)