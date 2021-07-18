from django.contrib import admin
from .models import Leaderboard


# Admin class for Profile
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
