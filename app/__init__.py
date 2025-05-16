from flask import Flask
from .config import Config
from .extensions import jwt, cors, dynamodb

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialiser les extensions
    jwt.init_app(app)
    cors.init_app(app)


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
