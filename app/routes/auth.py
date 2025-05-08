from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, set_refresh_cookies, unset_jwt_cookies, create_access_token
from app.services.auth_service import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = register_user(data['username'], data['password'])
        return jsonify(msg="Utilisateur créé", id=user.id), 201
    except ValueError as e:
        return jsonify(msg=str(e)), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    access, refresh = authenticate_user(data['username'], data['password'])
    if not access:
        return jsonify(msg="Identifiants invalides"), 401
    resp = jsonify(msg="Login OK")
    set_refresh_cookies(resp, refresh)
    resp.set_cookie('access_token_cookie', access, httponly=True, samesite='Strict', path='/api/')
    return resp

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)
    resp = jsonify(msg="Token rafraîchi")
    resp.set_cookie('access_token_cookie', access, httponly=True, samesite='Strict', path='/api/')
    return resp

@auth_bp.route('/logout', methods=['POST'])
def logout():
    resp = jsonify(msg="Déconnecté")
    unset_jwt_cookies(resp)
    return resp