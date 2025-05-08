# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import db, jwt, cors


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Log database connection on startup
    with app.app_context():
        try:
            engine = db.get_engine()
            conn = engine.connect()
            app.logger.info(f"Connecté à la base de données : {engine.url}")
            conn.close()
        except Exception as e:
            app.logger.error(f"Impossible de se connecter à la base : {e}")

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.protected import protected_bp
    from .routes.health import health_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(protected_bp, url_prefix="/api")
    app.register_blueprint(health_bp)

    return app