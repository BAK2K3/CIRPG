from django.contrib import admin
from .models import ActiveEnemy


# Admin class for Active Enemy
class EnemyAdmin(admin.ModelAdmin):
    """
    Profile Admin settiings for list display and ordering.
    """
    list_display = (
        'pk',
        'active_character',
        'enemy_id',
        'enemy_level',
        'weapon_id',
        'weapon_level'
    )

    ordering = ('pk',)


# Register the models
admin.site.register(ActiveEnemy, EnemyAdmin)
