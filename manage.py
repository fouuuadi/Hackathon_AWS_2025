from app import create_app
from flask_migrate import Migrate
from app.extensions import db

app = create_app()
migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5005, debug=True)
    
# manage.py
# from app import create_app
# from app.extensions import db
# from flask_migrate import Migrate

# # Création de l'application
# app = create_app()
# # Initialisation des migrations
# migrate = Migrate(app, db)