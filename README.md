````markdown
# Backend_Hackathon_AWS

API **Flask** + **React** + **PostgreSQL**

---

## Prérequis

- **Python 3.11**  
- **Node.js & npm** (pour le frontend)  
- **Docker & Docker Compose** (optionnel, pour la mise en place rapide de la base)

---

## Installation locale

1. **Clone** le dépôt et place-toi dans le dossier backend :
   ```bash
git clone https://…/ton-projet.git
cd ton-projet/backend_hackathon
````

2. **Crée** et **active** un environnement virtuel :

   ```bash
   ```

python3.11 -m venv venv

# Linux / macOS

source venv/bin/activate

# Windows (PowerShell)

.\venv\Scripts\Activate.ps1

````
3. **Installe** les dépendances Python :
   ```bash
pip install --upgrade pip
pip install -r requirements.txt
# ou, si tu préfères :
pip3 install --upgrade pip
pip3 install -r requirements.txt
````

4. **Configure** l’accès à la base PostgreSQL (Supabase) :
   Crée un fichier `.env` à la racine :

   ```ini
   ```

DATABASE\_URL=postgresql://postgres.<project-ref>:<PASSWORD>@aws-0-eu-west-1.pooler.supabase.com:5432/postgres?sslmode=require
SECRET\_KEY=\<clé\_aleatoire>

````
5. **Initialise** et **applique** les migrations :
   ```bash
export FLASK_APP=manage.py
flask db init      # une seule fois
flask db migrate
flask db upgrade
````

6. **Démarre** le serveur :

   ```bash
   ```

python3 manage.py

```
L’API écoute alors sur http://localhost:5005
```
