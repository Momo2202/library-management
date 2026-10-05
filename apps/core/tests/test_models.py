"""
Tests unitaires pour les modèles abstraits de l'app `core`.

Ces tests vérifient la structure des modèles abstraits
(TimeStampedModel, UUIDModel, BaseModel) sans créer
de modèles concrets, ce qui évite les problèmes de migrations.
"""

from django.db import models
from django.test import SimpleTestCase

from apps.core.models import BaseModel, TimeStampedModel, UUIDModel


# ============================================
# TimeStampedModel
# ============================================

class TimeStampedModelTest(SimpleTestCase):
    """Tests pour le modèle abstrait TimeStampedModel."""

    def test_est_abstrait(self):
        """TimeStampedModel doit être abstrait (pas de table)."""
        self.assertTrue(TimeStampedModel._meta.abstract)

    def test_champ_created_at_existe(self):
        """Le champ created_at doit exister."""
        champ_names = [f.name for f in TimeStampedModel._meta.fields]
        self.assertIn("created_at", champ_names)

    def test_champ_updated_at_existe(self):
        """Le champ updated_at doit exister."""
        champ_names = [f.name for f in TimeStampedModel._meta.fields]
        self.assertIn("updated_at", champ_names)

    def test_created_at_auto_now_add(self):
        """created_at doit être en auto_now_add (non modifiable)."""
        champ = TimeStampedModel._meta.get_field("created_at")
        self.assertTrue(champ.auto_now_add)

    def test_updated_at_auto_now(self):
        """updated_at doit être en auto_now (modifié à chaque save)."""
        champ = TimeStampedModel._meta.get_field("updated_at")
        self.assertTrue(champ.auto_now)

    def test_ordering_par_defaut(self):
        """Le tri par défaut doit être sur -created_at (du plus récent)."""
        self.assertEqual(TimeStampedModel._meta.ordering, ["-created_at"])


# ============================================
# UUIDModel
# ============================================

class UUIDModelTest(SimpleTestCase):
    """Tests pour le modèle abstrait UUIDModel."""

    def test_est_abstrait(self):
        """UUIDModel doit être abstrait."""
        self.assertTrue(UUIDModel._meta.abstract)

    def test_champ_id_existe(self):
        """Le champ `id` doit exister."""
        champ_id = UUIDModel._meta.get_field("id")
        self.assertIsNotNone(champ_id)

    def test_id_est_cle_primaire(self):
        """Le champ `id` doit être la clé primaire."""
        champ_id = UUIDModel._meta.get_field("id")
        self.assertTrue(champ_id.primary_key)

    def test_id_est_uuid(self):
        """Le champ `id` doit être de type UUIDField."""
        champ_id = UUIDModel._meta.get_field("id")
        self.assertIsInstance(champ_id, models.UUIDField)

    def test_id_non_editable(self):
        """Le champ `id` ne doit pas être éditable."""
        champ_id = UUIDModel._meta.get_field("id")
        self.assertFalse(champ_id.editable)


# ============================================
# BaseModel
# ============================================

class BaseModelTest(SimpleTestCase):
    """Tests pour le modèle abstrait BaseModel."""

    def test_est_abstrait(self):
        """BaseModel doit être abstrait."""
        self.assertTrue(BaseModel._meta.abstract)

    def test_herite_de_uuid_model(self):
        """BaseModel doit hériter de UUIDModel."""
        self.assertTrue(issubclass(BaseModel, UUIDModel))

    def test_herite_de_time_stamped_model(self):
        """BaseModel doit hériter de TimeStampedModel."""
        self.assertTrue(issubclass(BaseModel, TimeStampedModel))

    def test_possede_tous_les_champs(self):
        """BaseModel doit avoir id, created_at et updated_at."""
        champ_names = [f.name for f in BaseModel._meta.fields]
        self.assertIn("id", champ_names)
        self.assertIn("created_at", champ_names)
        self.assertIn("updated_at", champ_names)