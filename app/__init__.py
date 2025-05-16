# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import jwt, cors, mongo


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    #db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    mongo.init_app(app)

# --- Vérification / création de la base MongoDB ---
    with app.app_context():
        # Nom de la DB configurée (dernière partie de MONGO_URI)
        db_name = mongo.db.name
        client  = mongo.cx  # instance de MongoClient

        # Récupère la liste existante des databases
        existing_dbs = client.list_database_names()

        if db_name not in existing_dbs:
            # Crée directement la collection principale (ex. users)
            client[db_name].create_collection('users')
            print(f"📦 Base MongoDB '{db_name}' créée avec collection 'users'.")
        else:
            print(f"✔️  Base MongoDB '{db_name}' déjà présente.")


    # Register blueprints
    from .routes.card import card_bp
    from .routes.auth import auth_bp
    from .routes.protected import protected_bp
    from .routes.health import health_bp
    app.register_blueprint(card_bp, url_prefix="/api/cards")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(protected_bp, url_prefix="/api")
    app.register_blueprint(health_bp)

    return app