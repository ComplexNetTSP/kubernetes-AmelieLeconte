# Utilise une image officielle Python comme image de base
FROM python:3.9-slim

# Crée un répertoire de travail
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt .
# Installe les dépendances
RUN pip install -r requirements.txt

# Copie le code de l'application dans le conteneur
COPY . .

# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]
