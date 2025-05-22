#!/bin/bash

# Attendre que Keycloak soit complètement démarré
echo "Attente du démarrage complet de Keycloak..."
while ! curl -s http://keycloak:8080 > /dev/null; do
    echo "En attente de Keycloak..."
    sleep 5
done
echo "Keycloak est démarré."

# Appliquer les migrations
echo "Application des migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Créer un superuser si nécessaire
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser créé.')
else:
    print('Superuser existe déjà.')
"

# Démarrer l'application
echo "Démarrage de l'application Django..."
gunicorn core.wsgi:application --bind 0.0.0.0:8001 --workers 3
