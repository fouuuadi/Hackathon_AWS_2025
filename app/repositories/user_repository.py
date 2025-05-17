from app.extensions import mongo
from werkzeug.security import generate_password_hash, check_password_hash

USERS = mongo.db.user

def get_by_username(username: str):
    doc = USERS.find_one({"username": username})
    if not doc:
        return None
    return {
        "id":       str(doc["_id"]),
        "username": doc["username"],
        "password": doc["password"]
    }

def create_user(username: str, password: str):
    pw_hash = generate_password_hash(password)
    res     = USERS.insert_one({
        "username": username,
        "password": pw_hash
    })
    return {
        "id":       str(res.inserted_id),
        "username": username,
        "password": pw_hash
    }
