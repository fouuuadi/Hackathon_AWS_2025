from flask import Flask
from .config import Config
from .extensions import jwt, cors, dynamodb

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialiser les extensions
    jwt.init_app(app)
    cors.init_app(app)

    # Créer la table si elle n'existe pas
    table_name = app.config["DYNAMODB_TABLE_NAME"]
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {"AttributeName": "id", "KeyType": "HASH"}
            ],
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"}
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5
            }
        )
        table.wait_until_exists()
        print(f"📦 Table '{table_name}' créée avec succès.")
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        print(f"✔️ Table '{table_name}' déjà présente.")

    # Enregistrer les blueprints
    from .routes.card import card_bp
    from .routes.auth import auth_bp
    from .routes.protected import protected_bp
    from .routes.health import health_bp
    app.register_blueprint(card_bp, url_prefix="/api/cards")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(protected_bp, url_prefix="/api")
    app.register_blueprint(health_bp)

    return app
