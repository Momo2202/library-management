"""
Configuration Django pour l'environnement de développement.

Activée uniquement en local sur la machine du développeur.
"""

from .base import *  # noqa: F403

# ============================================
# MODE DEBUG
# ============================================

DEBUG = True

# En développement, on accepte tous les hosts
ALLOWED_HOSTS = ["*"]

# ============================================
# BASE DE DONNÉES
# ============================================

# Surcharge pour le développement (sera lue depuis .env)
DATABASES = {
    "default": env.db("DATABASE_URL"),  # noqa: F405
}
DATABASES["default"]["ENGINE"] = "django.db.backends.mysql"

# ============================================
# APPS DE DÉVELOPPEMENT
# ============================================

INSTALLED_APPS += [  # noqa: F405
    "django.contrib.admindocs",
]

# ============================================
# EMAIL (console en dev)
# ============================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"