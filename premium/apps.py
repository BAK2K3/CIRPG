"""
Premium App - Apps
----------------

App Configuration for Premium App.
"""

from django.apps import AppConfig


class PremiumConfig(AppConfig):
    """Premium App configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'premium'
