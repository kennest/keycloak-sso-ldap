"""
Django settings for core project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-j6z$3_3sg7$!^4+h7n*e*4%$$7pke5r4xwwep=i1g8o3g+5puy"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mozilla_django_oidc",  # OIDC
    "dashboard",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "mozilla_django_oidc.middleware.SessionRefresh",  # OIDC session refresh
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "dashboard.context_processors.auth_context",  # Ajoute des infos d'authentification
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# OIDC Authentication settings
AUTHENTICATION_BACKENDS = (
    "dashboard.auth.KeycloakOIDCAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# Keycloak OIDC settings
OIDC_RP_CLIENT_ID = "django-app"
OIDC_RP_CLIENT_SECRET = "S2ZMMUrBTDoDD34w8vpGs4QmC6KEMcnT"
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_OP_JWKS_ENDPOINT = (
    "http://keycloak:8080/realms/myrealm/protocol/openid-connect/certs"
)
OIDC_OP_AUTHORIZATION_ENDPOINT = (
    "http://keycloak:8080/realms/myrealm/protocol/openid-connect/auth"
)
OIDC_OP_TOKEN_ENDPOINT = (
    "http://keycloak:8080/realms/myrealm/protocol/openid-connect/token"
)
OIDC_OP_USER_ENDPOINT = (
    "http://keycloak:8080/realms/myrealm/protocol/openid-connect/userinfo"
)
OIDC_OP_LOGOUT_ENDPOINT = (
    "http://keycloak:8080/realms/myrealm/protocol/openid-connect/logout"
)

# Redirection settings
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

# OIDC Session settings
OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = 900  # 15 minutes

# Dans settings.py
# OIDC_CLAIMS_VERIFICATION = "dashboard.auth.verify_claims"  # Fonction personnalisée

# Désactiver certaines vérifications strictes
OIDC_VERIFY_SSL = False  # En développement seulement
OIDC_RP_SCOPES = (
    "openid email profile"  # Assurez-vous de demander les scopes nécessaires
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "mozilla_django_oidc": {
            "handlers": ["console"],
            "level": "DEBUG",
        }
    },
}
