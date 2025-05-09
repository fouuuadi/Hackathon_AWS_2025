from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Initialisation du blueprint "protected" pour regrouper les routes nécessitant une authentification
protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected', methods=['GET'])
@jwt_required()  # Nécessite un access token JWT valide en cookie ou en header
def protected():
    """
    Exemple de route protégée.
    Retourne l'ID de l'utilisateur authentifié.
    """
    # Récupère l'identité (ici l'ID utilisateur) depuis le JWT
    user_id = get_jwt_identity()
    # Renvoie un JSON avec l'ID récupéré
    return jsonify(logged_in_as=user_id)
