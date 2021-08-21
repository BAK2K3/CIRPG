"""
Profiles App - Apps
----------------

App Configuration for Profiles App.
"""

# pylint: disable=C0415,W0611

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Profiles App configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        """Import signals when configured."""
        import profiles.signals # noqa
