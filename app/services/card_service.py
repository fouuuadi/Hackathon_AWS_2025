from flask import Blueprint, request, jsonify
from app.services.card_service import create_card_with_board

# Blueprint pour gérer les cartes
card_bp = Blueprint('card', __name__)

@card_bp.route('/cards', methods=['POST'])
def create_card_route():
    """
    Endpoint pour créer une carte et l'associer à un board.
    Attends un JSON avec :
      - url, text, img, note (string), tags, resume_information, board_name
    Retourne :
      {
        "card": { ... },
        "board": { ... }  # ou null si pas de board_name fourni
      }
    """
    data = request.get_json()
    card, board = create_card_with_board(data)
    response = {"card": card}
    if board:
        response["board"] = board
    return jsonify(response), 201

@card_bp.route('/cards/<card_id>', methods=['GET'])
def get_card_route(card_id):
    """
    Récupère une carte par son ID.
    Renvoie 200 + card JSON ou 404 si introuvable.
    """
    from app.repositories.card_repository import get_card
    card = get_card(card_id)
    if not card:
        return jsonify(msg="Card not found"), 404
    return jsonify(card), 200
