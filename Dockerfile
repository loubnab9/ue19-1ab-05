# Utilise une image de base officielle de Python, légère
FROM python:3.7-slim-buster

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier de dépendances et les installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le fichier de l'application
COPY app.py .

# Définit la commande à exécuter au lancement du conteneur
CMD ["python", "app.py"]
