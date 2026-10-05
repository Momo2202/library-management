"""
Tests vérifiant que la configuration des tests est correcte.

Ces tests servent de garde-fous : si quelqu'un casse la config
des tests (par exemple en remettant MySQL), ces tests échouent.
"""

from django.conf import settings
from django.test import SimpleTestCase


class TestDatabaseSettings(SimpleTestCase):
    """Vérifie la configuration de la base de données de test."""

    def test_utilise_sqlite(self):
        """La base de données de test doit être SQLite."""
        engine = settings.DATABASES["default"]["ENGINE"]
        self.assertEqual(engine, "django.db.backends.sqlite3")

    def test_base_en_memoire(self):
        """
        La base de test doit être en mémoire RAM.

        Note : Django 5.x transforme automatiquement ":memory:"
        en 'file:memorydb_default?mode=memory&cache=shared'
        pour permettre le partage entre connexions.
        On vérifie donc juste que c'est bien une base en mémoire.
        """
        name = settings.DATABASES["default"]["NAME"]
        # Soit le nom exact, soit la version transformée par Django
        self.assertTrue(
            name == ":memory:" or "mode=memory" in name,
            f"La base n'est pas en mémoire : {name}",
        )


class TestSecuritySettings(SimpleTestCase):
    """Vérifie la configuration de sécurité des tests."""

    def test_hashage_mdp_rapide(self):
        """
        Le hashage des mots de passe doit être accéléré (MD5).

        En production, on utilise PBKDF2 (lent mais sûr).
        En test, on utilise MD5 (rapide mais non sécurisé)
        car la sécurité n'est pas l'objectif.
        """
        self.assertIn(
            "django.contrib.auth.hashers.MD5PasswordHasher",
            settings.PASSWORD_HASHERS,
        )

    def test_debug_force_a_false(self):
        """
        Django force DEBUG=False pendant les tests, quelle que soit
        la config dans les settings. C'est un garde-fou de sécurité.

        Ce test vérifie que ce comportement est bien respecté :
        si un jour Django change, on veut le savoir.
        """
        self.assertFalse(settings.DEBUG)