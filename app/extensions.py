from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Instances, pas encore liées à app
db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()