from dotenv import load_dotenv
import os

load_dotenv()  # charge .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = True
    CORS_SUPPORTS_CREDENTIALS = True

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True