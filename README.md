   # Backend_Hackathon_AWS

   # Backend Flask + React + PostgreSQL

   ## Prérequis

   - Python 3.11
   - Node.js / npm (pour le frontend)
   - Docker & Docker Compose (optionnel)

   ## Installation

   1. Clone le dépôt  
      ```bash
      git clone https://…/ton-projet.git
      cd ton-projet/backend_hackathon

   2. Crée et active l’environnement virtuel

   python3.11 -m venv venv
   source venv/bin/activate        # Linux/macOS
   # ou .\venv\Scripts\Activate.ps1 # Windows PowerShell

   3. Installe les dépendances Python

   pip install --upgrade pip
   pip install -r requirements.txt
   ou
   pip3 install --upgrade pip
   pip3 install -r requirements.txt


   4. Configure l’accès à la DB avec supabase

   Crée un fichier .env à la racine :

   DATABASE_URL=postgresql://postgres.<project-ref>:<PASSWORD>@aws-0-eu-west-1.pooler.supabase.com:5432/postgres?sslmode=require
   SECRET_KEY=<clé_aleatoire>

   5. Initialise et applique les migrations

   export FLASK_APP=manage.py
   flask db init      # une seule fois
   flask db migrate
   flask db upgrade

   6. Demarre le serveur

   python3 manage.py



