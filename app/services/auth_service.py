from flask_jwt_extended import create_access_token, create_refresh_token
from app.repositories.user_repository import get_by_username, create_user

def register_user(username, password):
    existing = get_by_username(username)
    if existing:
        raise ValueError("Username already taken")
    return create_user(username, password)


def authenticate_user(username: str, password: str):
    """
    Vérifie les credentials et renvoie (access_token, refresh_token)
    avec identity au format string pour flask-jwt-extended.
    """
    user = get_by_username(username)
    if user and user.check_password(password):
        sub = str(user.id)  # identity doit être une string
        access = create_access_token(identity=sub)
        refresh = create_refresh_token(identity=sub)
        return access, refresh
    return None, None

# def authenticate_user(username, password):
#     user = get_by_username(username)
#     if user and user.check_password(password):
#         access = create_access_token(identity=user.id)
#         refresh = create_refresh_token(identity=user.id)
#         return access, refresh
#     return None, None