import boto3
from werkzeug.security import generate_password_hash, check_password_hash
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()

# Chargement du nom de la table depuis .env
TABLE_NAME = os.getenv("DYNAMODB_TABLE_USERS", "users")
dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')  # adapte la région si besoin
USERS = dynamodb.Table(TABLE_NAME)

def get_by_username(username: str):
    try:
        response = USERS.get_item(Key={"username": username})
    except ClientError as e:
        print("Erreur DynamoDB:", e.response['Error']['Message'])
        return None

    if "Item" not in response:
        return None

    item = response["Item"]
    return {
        "username": item["username"],
        "password": item["password"]
    }

def create_user(username: str, password: str):
    pw_hash = generate_password_hash(password)

    try:
        USERS.put_item(Item={
            "username": username,
            "password": pw_hash
        })
    except ClientError as e:
        print("Erreur DynamoDB:", e.response['Error']['Message'])
        return None

    return {
        "username": username,
        "password": pw_hash
    }
