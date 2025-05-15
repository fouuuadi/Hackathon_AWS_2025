from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash
from app.repositories.user_repository import get_by_username, create_user

# Service d'authentification : contenu de la logique métier

def register_user(username, password):
    """
    Inscrit un nouvel utilisateur si le nom est disponible.
    - Vérifie si le username existe déjà en base.
    - Lève une ValueError si déjà pris.
    - Sinon, délègue la création à user_repository.create_user et renvoie le nouvel objet User.
    """
    existing = get_by_username(username)
    if existing:
        # Empêche la création de doublon de nom d'utilisateur
        raise ValueError("Username already taken")
    # Crée et retourne l'utilisateur
    return create_user(username, password)


def authenticate_user(username: str, password: str):
    """
    Authentifie un utilisateur :
    - Récupère l'utilisateur en base.
    - Vérifie le mot de passe via la méthode model.check_password().
    - Si valide :
        * Convertit l'ID en string (requis par flask-jwt-extended).
        * Génère un access token (court terme).
        * Génère un refresh token (long terme).
        * Renvoie le tuple (access, refresh).
    - Si échec : renvoie (None, None).
    """
    # Recherche en base l'utilisateur par son username
    user = get_by_username(username)
    # Vérifie à la fois existence et validité du mot de passe
    if user and check_password_hash(user["password"], password):
        # Flask-JWT-Extended exige que l'identity soit une chaîne
        sub = str(user["id"])
        # Génération du JWT d'accès
        access = create_access_token(identity=sub)
        # Génération du JWT de rafraîchissement
        refresh = create_refresh_token(identity=sub)
        return access, refresh
    # Authentification échouée
    return None, None

# Version alternative commentée :
# def authenticate_user(username, password):
#     user = get_by_username(username)
#     if user and user.check_password(password):
#         access = create_access_token(identity=user.id)
#         refresh = create_refresh_token(identity=user.id)
#         return access, refresh
#     return None, None
