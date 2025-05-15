from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    set_refresh_cookies,
    unset_jwt_cookies,
    create_access_token
)
from app.services.auth_service import register_user, authenticate_user

# Initialisation du blueprint "auth" pour regrouper les routes d'authentification
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Inscription d'un nouvel utilisateur.
    Attends un JSON { username, password }.
    Renvoie 201 + { msg, id } ou 400 en cas d'erreur (username déjà pris).
    """
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify(msg="Username & password requis"), 400
    try:
        user = register_user(data['username'], data['password'])
        return jsonify(msg="Utilisateur créé", id=user["id"]), 201
    except ValueError as e:
        return jsonify(msg=str(e)), 400
    except Exception as e:
        print(f"Erreur création user : {e}")
        return jsonify(msg="Erreur interne"), 500
    
@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Connexion d'un utilisateur.
    Attends un JSON { username, password }.
    Renvoie un JSON 200 + cookies JWT (access & refresh) ou 401 si identifiants invalides.
    """
    data = request.get_json()
    # Authentifie et récupère tokens
    access, refresh = authenticate_user(data['username'], data['password'])
    if not access:
        # Identifiants incorrects
        return jsonify(msg="Identifiants invalides"), 401
    # Préparation de la réponse avec message
    resp = jsonify(msg="Login OK")
    # Stocke le refresh token en cookie HTTP-only
    set_refresh_cookies(resp, refresh)
    # Stocke l'access token en cookie HTTP-only, soumis sur /api/*
    resp.set_cookie(
        'access_token_cookie', access,
        httponly=True,
        samesite='Strict',
        path='/api/'
    )
    return resp

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """
    Rafraîchissement du token d'accès.
    Nécessite un refresh token valide en cookie.
    Renvoie un nouvel access token en cookie.
    """
    # Récupère l'identity depuis le refresh token
    identity = get_jwt_identity()
    # Génère un nouveau access token
    access = create_access_token(identity=identity)
    resp = jsonify(msg="Token rafraîchi")
    # Remplace l'ancien access token
    resp.set_cookie(
        'access_token_cookie', access,
        httponly=True,
        samesite='Strict',
        path='/api/'
    )
    return resp

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """
    Déconnexion de l'utilisateur.
    Efface les cookies JWT (access & refresh) côté client.
    """
    resp = jsonify(msg="Déconnecté")
    # Supprime tous les cookies JWT générés
    unset_jwt_cookies(resp)
    return resp
