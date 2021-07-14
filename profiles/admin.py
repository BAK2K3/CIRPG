from django.contrib import admin
from .models import ActiveCharacter, Profile


# Admin class for Profile
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


# Admin class for Active Characters
class CharacterAdmin(admin.ModelAdmin):
    """
    Profile Admin settiings for list display and ordering.
    """
    list_display = (
        'pk',
        'user',
        'current_level',
        'current_xp',
        'battle_count',
        'character_id',
        'weapon_id',
    )

    ordering = ('pk',)


# Register the models
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ActiveCharacter, CharacterAdmin)
