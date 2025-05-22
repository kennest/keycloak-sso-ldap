FROM ubuntu:22.04

# Configuration des variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    PYTHON_VERSION=3.11

# Installation des dépendances système et Python
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    software-properties-common \
    curl \
    build-essential \
    libpq-dev \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

# Créer un lien symbolique pour python
RUN ln -sf /usr/bin/python3.11 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Configuration du répertoire de travail
WORKDIR /app

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste du code de l'application
COPY . .

# Rendre le script d'entrée exécutable
RUN chmod +x /app/entrypoint.sh

# Exposition du port
EXPOSE 8001

# Commande de démarrage (sera remplacée par celle dans docker-compose)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8001", "--workers", "3"]
