import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    FRONTEND_URL = os.getenv("FRONTEND_URL")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

   
    JWT_ACCESS_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
    JWT_ACCESS_TOKEN_EXPIRY_MINUTES = int(
    os.getenv("JWT_ACCESS_TOKEN_EXPIRY_MINUTES", 15)
    )

    JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")
    JWT_REFRESH_TOKEN_EXPIRY_DAYS = int(
    os.getenv("JWT_REFRESH_TOKEN_EXPIRY_DAYS", 7)
    )
    
    ENV = os.getenv("ENV", "development")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    FRONTEND_URL = os.getenv("FRONTEND_URL")