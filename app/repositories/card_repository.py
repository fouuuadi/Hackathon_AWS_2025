from bson.objectid import ObjectId
from app.extensions import mongo

# Accès à la collection "cards" dans MongoDB
CARDS = mongo.db.cards


def get_card(card_id: str) -> dict:
    """
    Récupère une carte par son ID.
    - card_id : chaîne de caractères de l'ObjectId Mongo.
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
        "url": doc.get("url"),
        "text": doc.get("text"),
        "img": doc.get("img"),
        "note": doc.get("note"),
        "tags": doc.get("tags", []),
        "resume_information": doc.get("resume_information")
    }


def create_card(data: dict) -> dict:
    """
    Crée une nouvelle carte.
    - data : dict contenant les clés url, text, img, note, tags, resume_information.
    - Insère le document en base et retourne le dict créé avec l'ID.
    """
    payload = {
        "url": data["url"],
        "text": data["text"],
        "img": data.get("img"),
        "note": data.get("note"),
        "tags": data.get("tags", []),
        "resume_information": data.get("resume_information")
    }
    # Insert et récupération de l'ID généré
    result = CARDS.insert_one(payload)
    payload["id"] = str(result.inserted_id)
    return payload
