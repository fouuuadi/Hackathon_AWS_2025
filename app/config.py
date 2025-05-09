from dotenv import load_dotenv  # pour charger les variables d'environnement depuis le fichier .env
import os

# Charge les variables définies dans .env au démarrage de l'application
load_dotenv()

class Config:
    """
    Configuration de base partagée par tous les environnements.
    Les variables sensibles (DB, clef secrète) sont lues depuis le .env.
    """
    # URL de connexion à la base PostgreSQL (SQLAlchemy)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # Clé secrète pour signer les JWT et sécuriser les sessions
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    # Emplacement des tokens JWT : ici, dans des cookies HTTP-only
    JWT_TOKEN_LOCATION = ['cookies']
    # Active la protection CSRF pour les cookies JWT
    JWT_COOKIE_CSRF_PROTECT = True
    # Autorise l'envoi de credentials (cookies) via CORS
    CORS_SUPPORTS_CREDENTIALS = True

class ProdConfig(Config):
    """
    Configuration spécifique à la production.
    """
    DEBUG = False  # désactive le mode debug pour plus de sécurité en prod

class DevConfig(Config):
    """
    Configuration spécifique au développement local.
    """
    DEBUG = True   # active le debug pour rechargement auto et messages d'erreur détaillés
