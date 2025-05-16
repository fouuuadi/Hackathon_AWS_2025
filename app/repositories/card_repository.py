import os
from app.extensions import dynamodb
from uuid import uuid4

TABLE_NAME = os.getenv("DYNAMODB_TABLE_CARDS", "cards")
table = dynamodb.Table(TABLE_NAME)


def get_card(card_id: str) -> dict:
    """
    Récupère une carte par son ID.
    """
    try:
        response = table.get_item(Key={"id": card_id})
        item = response.get("Item")
        if not item:
            return None
        return item
    except Exception as e:
        print(f"Erreur lors de la récupération de la carte : {e}")
        return None


def create_card(data: dict) -> dict:
    """
    Crée une nouvelle carte.
    """
    try:
        card_id = str(uuid4())
        data["id"] = card_id
        table.put_item(Item=data)
        return data
    except Exception as e:
        print(f"Erreur lors de la création de la carte : {e}")
        return None
