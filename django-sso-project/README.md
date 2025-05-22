# Django Keycloak SSO

Application Django utilisant Keycloak pour l'authentification SSO (Single Sign-On) avec une vue publique et une vue privée. Intégration LDAP pour la gestion des utilisateurs.

## Fonctionnalités

- Authentification via Keycloak
- Intégration LDAP
- Vue publique accessible à tous
- Vue privée accessible uniquement après connexion
- Interface utilisateur responsive avec Bootstrap 5

## Architecture

Le projet utilise Docker Compose pour orchestrer les services suivants :

- **Django** : Application web principale
- **Keycloak** : Serveur d'identité et d'authentification
- **PostgreSQL** : Base de données pour Keycloak
- **LDAP** : Serveur OpenLDAP pour la gestion des utilisateurs
- **phpLDAPadmin** : Interface d'administration LDAP

## Prérequis

- Docker et Docker Compose
- Git

## Installation et démarrage

1. Cloner le dépôt :

```bash
git clone <repository-url>
cd keycloak-sso-ldap/django-sso-project
```

2. Démarrer les services avec Docker Compose :

```bash
docker-compose up -d
```

3. Accéder aux différentes interfaces :
   - Application Django : <http://localhost:8001>
   - Keycloak : <http://localhost:8080> (admin/admin)
   - phpLDAPadmin : <http://localhost:8081> (cn=admin,dc=myorg,dc=local/admin)

## Configuration initiale de Keycloak

Pour que l'application fonctionne correctement, il faut configurer Keycloak :

1. Se connecter à l'interface d'administration Keycloak (<http://localhost:8080>) avec les identifiants admin/admin
2. Créer un client OAuth/OIDC pour l'application Django :
   - Nom : django-app
   - Type de client : Confidential
   - URL de redirection : <http://localhost:8001/oidc/callback/>
   - Secret : django-app-secret

3. Créer un Realm (ou utiliser le Realm "master")
4. Configurer l'intégration LDAP pour importer les utilisateurs

## Utilisation

1. Accéder à l'application Django : <http://localhost:8001>
2. La page d'accueil est publique
3. Cliquer sur "Se connecter" pour être redirigé vers Keycloak
4. Après authentification, vous accéderez au tableau de bord privé

## Structure du projet

```
django-sso-project/
├── app/                       # Application Django
│   ├── core/                  # Configuration du projet Django
│   ├── dashboard/             # Application pour les vues publiques et privées
│   ├── templates/             # Templates HTML
│   ├── static/                # Fichiers statiques
│   ├── Dockerfile             # Configuration Docker pour l'app Django
│   └── requirements.txt       # Dépendances Python
├── keycloak/                  # Configuration Keycloak
│   └── themes/                # Thèmes personnalisés
├── docker-compose.yml         # Configuration des services
└── README.md                  # Ce fichier
```

## Développement

Pour développer localement sans Docker :

1. Créer et activer un environnement virtuel Python
2. Installer les dépendances : `pip install -r app/requirements.txt`
3. Lancer le serveur de développement : `cd app && python manage.py runserver`

## Accès à l'administration Django

- URL : <http://localhost:8001/admin/>
- Identifiants par défaut : admin/admin
