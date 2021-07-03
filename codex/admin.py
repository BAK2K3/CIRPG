from django.contrib import admin
from .models import Codex


class CodexAdmin(admin.ModelAdmin):
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
