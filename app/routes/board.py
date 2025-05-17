# app/routes/board.py
from flask import Blueprint, request, jsonify
from app.repositories.board_repository import get_board_by_name, add_card_to_board, get_all_boards
from app.repositories.card_repository import get_card

board_bp = Blueprint('board', __name__)

@board_bp.route('/boards', methods=['GET'])
def list_boards_route():
    """
    Récupère la liste de tous les boards.
    URL : GET /api/boards
    Renvoie un tableau de dicts avec les champs id et name.
    """
    boards = get_all_boards()
    # On ne retourne que l'id et le nom du board
    result = [{"id": b["id"], "name": b["name"]} for b in boards]
    return jsonify(result), 200

@board_bp.route('/boards/<string:name>', methods=['GET'])
def get_board_route(name):
    board = get_board_by_name(name)
    if not board:
        return jsonify(msg="Board not found"), 404

    # Récupère chaque carte en base et remplace card_ids par un tableau de cartes
    cards = []
    for cid in board["card_ids"]:
        card = get_card(cid)
        if card:
            cards.append(card)

    # Réponse enrichie : on supprime card_ids et on fournit cards détaillées
    return jsonify({
        "id":        board["id"],
        "name":      board["name"],
        "cards":     cards
    }), 200


@board_bp.route('/boards/<name>/cards/<card_id>', methods=['POST'])
def add_card_to_board_route(name, card_id):
    """
    Ajoute une carte à un board.
    Returns 200 + le board mis à jour.
    """
    board = add_card_to_board(name, card_id)
    return jsonify(board), 200 