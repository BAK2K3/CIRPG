from django.contrib import admin
from .models import Profile


# Admin class for Codex
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile Admin settiings for list display and ordering.
    """
    list_display = (
        'pk',
        'user',
        'paid',
        'active_char',
        'active_battle',
        'total_runs',
        'longest_run',
    )

    ordering = ('pk',)


# Register the Codex model
admin.site.register(Profile, ProfileAdmin)
