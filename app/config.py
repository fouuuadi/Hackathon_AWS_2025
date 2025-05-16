from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """
    Configuration de base partagée par tous les environnements.
    """
    # Configuration DynamoDB
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    DYNAMODB_TABLE_USER = os.getenv("DYNAMODB_TABLE_USER")
    DYNAMODB_TABLE_CARD = os.getenv("DYNAMODB_TABLE_CARD")
    DYNAMODB_TABLE_BOARD = os.getenv("DYNAMODB_TABLE_BOARD")
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = True
    CORS_SUPPORTS_CREDENTIALS = True

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
