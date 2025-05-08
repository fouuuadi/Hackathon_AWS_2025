# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

# Installer system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt \
    || pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port de l'application
EXPOSE 5000

# Point d'entrée
ENV FLASK_APP=manage.py
CMD ["python3", "manage.py"]
