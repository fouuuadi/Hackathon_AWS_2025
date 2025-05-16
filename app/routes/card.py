# app/routes/card.py
from flask import Blueprint, request, jsonify
from app.repositories.card_repository import create_card, get_card

card_bp = Blueprint('card', __name__)

@card_bp.route('/cards', methods=['POST'])
def create_card_route():
    """
    Expects JSON body:
    {
      "url": "...",
      "text": "...",
      "img": "...",
      "note": 5,
      "tags": ["tag1","tag2"],
      "resume_information": "..."
    }
    Returns 201 + le document créé (avec son champ 'id').
    """
    data = request.get_json()
    card = create_card(data)
    return jsonify(card), 201

@card_bp.route('/cards/<card_id>', methods=['GET'])
def get_card_route(card_id):
    """
    Récupère la carte dont l'id est passé en URL.
    Returns 200 + le document ou 404 si introuvable.
    """
    card = get_card(card_id)
    if not card:
        return jsonify(msg="Card not found"), 404
    return jsonify(card), 200
