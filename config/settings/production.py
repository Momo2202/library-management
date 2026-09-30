"""
Configuration Django pour l'environnement de production.

Sécurité maximale, aucun debug, sources externes uniquement.
"""

from .base import *  # noqa: F403

# ============================================
# MODE DEBUG (JAMAIS en prod !)
# ============================================

DEBUG = False

# ============================================
# SÉCURITÉ
# ============================================

# Cookies sécurisés (HTTPS uniquement)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Autres protections
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# ============================================
# FICHIERS STATIQUES
# ============================================

# WhiteNoise sert les fichiers statiques directement par Django en prod
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ============================================
# LOGGING PRODUCTION
# ============================================

LOGGING["handlers"]["console"]["level"] = "WARNING"  # noqa: F405