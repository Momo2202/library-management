"""
Configuration Django commune à tous les environnements.

Ce module contient les paramètres partagés entre développement
et production. Les paramètres spécifiques sont définis dans
development.py et production.py.
"""

from pathlib import Path

import environ

# ============================================
# CHEMINS DE BASE
# ============================================

# BASE_DIR pointe vers la racine du projet (là où se trouve manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ============================================
# VARIABLES D'ENVIRONNEMENT
# ============================================

# Initialisation de django-environ pour lire le fichier .env
env = environ.Env(
    # Valeurs par défaut + types
    DEBUG=(bool, False),
    SECRET_KEY=(str, ""),
    ALLOWED_HOSTS=(list, []),
    DATABASE_URL=(str, ""),
)

# Lecture du fichier .env s'il existe
env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(env_file)

# ============================================
# SÉCURITÉ
# ============================================

# Clé secrète (obligatoirement définie dans .env en prod)
SECRET_KEY = env("SECRET_KEY")

# Hôtes autorisés
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# ============================================
# APPLICATIONS
# ============================================

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Applications tierces
THIRD_PARTY_APPS = [
    # Ajoutées plus tard (prometheus, etc.)
]

# Applications locales (notre code)
# Note : chaque app sera ajoutée ici au fur et à mesure
LOCAL_APPS = [
    "apps.core",
    # "apps.authors",
    # "apps.books",
    # "apps.members",
    # "apps.loans",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ============================================
# MIDDLEWARES
# ============================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ============================================
# URLS & WSGI
# ============================================

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# ============================================
# TEMPLATES
# ============================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Dossier global de templates (utilisé pour base.html, etc.)
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ============================================
# BASE DE DONNÉES
# ============================================

# La config réelle sera définie dans development.py et production.py
DATABASES = {
    "default": env.db("DATABASE_URL"),
}
DATABASES["default"]["ENGINE"] = "django.db.backends.mysql"

# ============================================
# VALIDATION DES MOTS DE PASSE
# ============================================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ============================================
# INTERNATIONALISATION
# ============================================

LANGUAGE_CODE = "fr-fr"  # Interface en français
TIME_ZONE = "Europe/Paris"  # Fuseau horaire français
USE_I18N = True
USE_TZ = True

# ============================================
# FICHIERS STATIQUES & MEDIA
# ============================================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ============================================
# DIVERS
# ============================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ============================================
# LOGGING
# ============================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
