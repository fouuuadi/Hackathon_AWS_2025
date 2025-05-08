# app/routes/health.py
from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extensions import db

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    try:
        # Utiliser text() pour envelopper la requête SQL
        db.session.execute(text("SELECT 1"))
        return jsonify(status='ok', db='connected'), 200
    except Exception as e:
        return jsonify(status='error',
                       db='disconnected',
                       message=str(e)), 500