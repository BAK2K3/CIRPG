"""
Leaderboard App - Apps
----------------

App Configuration for Leaderboard App.
"""

from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    """Leaderboard App configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leaderboard'
