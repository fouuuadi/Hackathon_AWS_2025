from app import create_app                    # Importe la factory pour créer l'instance Flask
from flask_migrate import Migrate               # Extension pour gérer les migrations Alembic
from app.extensions import dynamodb                   # Instance SQLAlchemy déclarée dans extensions

# Création de l'application à partir de la factory
app = create_app()
# Liaison de Flask-Migrate avec l'app et la base de données
migrate = Migrate(app, dynamodb)

# Route de test basique (Hello World) pour vérifier que l'app tourne
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

# Point d'entrée pour exécution directe via `python manage.py`
if __name__ == '__main__':
    # recrée l'app pour s'assurer que la factory est utilisée
    app = create_app()
    # lance le serveur de développement sur 0.0.0.0:5005 avec debug activé
    app.run(host='0.0.0.0', port=5005, debug=True)

# Note :
# - FLASK_APP=manage.py permet à la CLI `flask` de découvrir `app` pour les commandes.
# - La partie `if __name__ == '__main__'` est utilisée uniquement pour le démarrage direct.
