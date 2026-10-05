from django.db import models

import uuid

class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création",
        help_text="Date et heure de création de l'enregistrement"
    )
    updated_at=models.DateTimeField(
        auto_now=True,
        verbose_name="Date de mise à jour",
        help_text="Date et heure de la dernière mise à jour de l'enregistrement"
    )
    class Meta:
        abstract=True
        ordering=["-created_at"]

class UUIDModel(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Identifiant",
    )
    class Meta:
        abstract=True
    

class BaseModel(UUIDModel, TimeStampedModel):
    class Meta:
        abstract=True
        ordering=["-created_at"]