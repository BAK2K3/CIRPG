"""
Leaderboard App - Admin
----------------

Admin Configuration for Leaderboard App.
"""

from django.contrib import admin
from .models import Leaderboard


class LeaderboardAdmin(admin.ModelAdmin):
    """
    Leaderboard Admin settings for list display and ordering.
    """
    list_display = (
        'user',
        'score',
    )

    ordering = ('-score',)


# Register the models
admin.site.register(Leaderboard, LeaderboardAdmin)
