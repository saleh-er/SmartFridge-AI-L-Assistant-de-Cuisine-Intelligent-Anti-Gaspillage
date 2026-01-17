# 1. Image de base légère avec Python
FROM python:3.11-slim

# 2. Installation des dépendances système nécessaires pour l'IA (OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 4. Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du code
COPY . .

# 6. Lancer l'application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]