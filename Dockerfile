# syntax=docker/dockerfile:1

# Image de base légère avec Python 3.11
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port utilisé par manage.py (5005)
EXPOSE 5005

# Variables d'environnement par défaut (surchargées par docker-compose ou .env)
ENV FLASK_APP=manage.py
ENV FLASK_ENV=production

# Démarre l'application via manage.py (run direct, port 5005)
CMD ["python3", "manage.py"]
