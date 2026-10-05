"""
Configuration Django pour l'exécution des tests.

Ce fichier hérite de la configuration de développement
et remplace UNIQUEMENT la base de données par SQLite en mémoire.

Avantages :
- Tests ultra-rapides (pas d'I/O disque)
- Aucune dépendance externe (pas besoin de MySQL)
- Isolation parfaite (base détruite à la fin de chaque session)

Note : La compatibilité MySQL est validée dans la CI/CD
via une pipeline dédiée.
"""

from .development import *

# ============================================
# BASE DE DONNÉES DE TEST
# ============================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # Base en mémoire RAM (extrêmement rapide)
        # ":memory:" est détruit à la fin de la session de tests
        "NAME": ":memory:",
    }
}

# ============================================
# OPTIMISATIONS POUR TESTS
# ============================================

# Hashage des mots de passe accéléré (10x plus rapide)
# ⚠️ À N'UTILISER QUE POUR LES TESTS
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Désactive le logging pendant les tests (moins de bruit)
LOGGING["root"]["level"] = "CRITICAL"
