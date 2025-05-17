from bson.objectid import ObjectId
from app.extensions import mongo
from app.repositories.board_repository import add_card_to_board

# Accès à la collection "cards" dans MongoDB
CARDS = mongo.db.card


def get_card(card_id: str) -> dict:
    """
    Récupère une carte par son ID.
    - card_id : chaîne de caractères de l'ObjectId Mongo.
    - note : texte libre (string) fournissant un commentaire ou une note.
    - Retourne un dict standardisé ou None si introuvable.
    """
    try:
        doc = CARDS.find_one({"_id": ObjectId(card_id)})
    except Exception:
        return None
    if not doc:
        return None

    # Retourner un document avec l'ID sous forme de string
    return {
        "id": str(doc["_id"]),
        "title": doc.get("title"),
        "url": doc.get("url"),
        "text": doc.get("text"),
        "img": doc.get("img"),
        "note": doc.get("note"),  # note libre (string) notée par l'utilisateur
        "board_name": doc.get("board_name"),
        "tags": doc.get("tags", []),
        "resume_information": doc.get("resume_information")
    }


def create_card(data: dict) -> dict:
    """
    Crée une nouvelle carte.
    - data : dict contenant les clés title, url, text, img, note (string), tags, resume_information.
    - note : texte libre (string) pour la carte.
    Insère le document en base et retourne le dict créé avec l'ID.
    """
    payload = {
        "title": data.get("title", ""),
        "url": data["url"],
        "text": data["text"],
        "img": data.get("img"),
        "note": data.get("note"),  # note libre (string) saisie par l'utilisateur
        "board_name": data.get("board_name"),
        "tags": data.get("tags", []),
        "resume_information": data.get("resume_information")
    }
    # Insert et récupération de l'ID généré
    result = CARDS.insert_one(payload)
    payload["id"] = str(result.inserted_id)
    return payload


def create_card_with_board(data: dict) -> tuple[dict, dict]:
    """
    Crée une carte et l'ajoute à un board si board_name est spécifié.
    Retourne un tuple (card, board) où board peut être None.
    """
    # Création de la carte avec board_name déjà dans le payload
    card = create_card(data)

    board = None
    board_name = data.get("board_name")
    if board_name:
        # Lie (ou crée) le board du même nom
        board = add_card_to_board(board_name, card["id"])

    return card, board
