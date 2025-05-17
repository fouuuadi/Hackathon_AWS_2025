from bson.objectid import ObjectId
from app.extensions import mongo

# Accès à la collection "boards" dans MongoDB
# (veillez à utiliser le même nom que dans votre base : 'boards' ou 'board')
BOARDS = mongo.db.board

def get_all_boards() -> list[dict]:
    """
    Récupère tous les boards existants.
    Renvoie une liste de dicts standardisés : { 'id': str, 'name': str }.
    """
    docs = BOARDS.find()
    return [
        {
            "id":   str(doc["_id"]),
            "name": doc["name"]
        }
        for doc in docs
    ]

def get_board_by_name(name: str) -> dict | None:
    """
    Récupère un board par son nom.
    - name : nom du board recherché.
    Renvoie un dict standardisé ou None si pas trouvé.
    """
    # Recherche d'un document dont le champ 'name' correspond
    doc = BOARDS.find_one({"name": name})
    if not doc:
        # Aucun board trouvé avec ce nom
        return None
    # Retourne un dict plus simple, avec l'ID converti en string
    return {
        "id": str(doc["_id"]),
        "name": doc["name"],
        # On convertit chaque ObjectId de la liste en string
        "card_ids": [str(cid) for cid in doc.get("card_ids", [])]
    }


def add_card_to_board(board_name: str, card_id: str) -> dict:
    """
    Ajoute un card_id à un board existant, ou crée un nouveau board.
    - board_name : nom du board où on veut ajouter la carte.
    - card_id    : ID de la carte (string) à associer.
    Retourne le dict du board (créé ou mis à jour).
    """
    # On cherche d'abord si le board existe déjà
    board = BOARDS.find_one({"name": board_name})
    if board:
        # Utilise $addToSet pour ne pas dupliquer la même carte
        BOARDS.update_one(
            {"name": board_name},
            {"$addToSet": {"card_ids": ObjectId(card_id)}}
        )
        # Puis renvoie le board mis à jour
        return get_board_by_name(board_name)

    # Si le board n'existe pas, on le crée avec la première carte
    result = BOARDS.insert_one({
        "name": board_name,
        "card_ids": [ObjectId(card_id)]
    })
    # Retourne le nouveau board sous forme de dict
    return {
        "id": str(result.inserted_id),
        "name": board_name,
        "card_ids": [card_id]
    }

