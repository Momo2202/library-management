"""
Configuration de l'application core

Cette app contient les elements partagé par toutes les autres:
-Modeles abstraits(TimeStampedModel,UUIDModel)
-Mixins Reutilisables
-Templates de base
- Utilitaires communs
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    verbose_name = "Coeur du système"
