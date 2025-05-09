from flask_sqlalchemy import SQLAlchemy  # ORM pour gérer la base de données relationnelle
from flask_jwt_extended import JWTManager  # Gestion de la génération et validation des JWT
from flask_cors import CORS                # Autoriser le partage de ressources cross-origin (front React)

# Déclaration des instances d'extensions, sans les attacher à une application Flask
# L'attachement se fait ensuite via db.init_app(app), jwt.init_app(app), cors.init_app(app)

# Instance SQLAlchemy pour la gestion des modèles et sessions DB
db = SQLAlchemy()

# Instance JWTManager pour configurer flask-jwt-extended (tokens, callbacks)
jwt = JWTManager()

# Instance CORS pour autoriser les requêtes cross-domain (avec credentials)
cors = CORS()
