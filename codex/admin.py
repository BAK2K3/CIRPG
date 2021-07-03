from django.contrib import admin
from .models import Codex


# Admin class for Codex
class CodexAdmin(admin.ModelAdmin):
    """
    Codex Admin settiings for list display and ordering.
    """
    list_display = (
        'pk',
        'name',
        'alpha_name',
        'type',
        'base_hp',
        'base_attack',
        'base_defense',
        'base_speed',
        'paid',
        'min_level'
    )

    ordering = ('pk',)


# Register the Codex model
admin.site.register(Codex, CodexAdmin)
