import boto3
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Recup les secrets depuis AWS Secrets Manager
import json
import os
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "lightsail/dynamodb/credentials"
    region_name = os.getenv("AWS_REGION", "eu-west-3")

    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response["SecretString"])
    except ClientError as e:
        print(f"Erreur lors de la récupération du secret: {e}")
        raise e


# Recup les secrets
secrets = get_secret()

# Init les extensions
dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION", "eu-west-3"),
    aws_access_key_id=secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=secrets["AWS_SECRET_ACCESS_KEY"]
)
# Instance JWTManager pour configurer flask-jwt-extended (tokens, callbacks)
jwt = JWTManager()
# Instance CORS pour autoriser les requêtes cross-domain (avec credentials)
cors = CORS()

