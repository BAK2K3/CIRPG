from django.db import models
from codex.models import Codex
from profiles.models import ActiveCharacter
from django.utils.translation import gettext_lazy as _


# Create your models here.

class ActiveEnemy(models.Model):

    """
    Active Enemy Model
    -----------

    Model for active Enemy.
    These are created and stored when
    a user engages in battle. The entry
    is removed when a battle is finished.

    active_character:
        Associated Active Character
    enemy_id:
        Foreign Key to Hero in DB
    enemy_(various):
        Modified stats associated with hero
    weapon_id:
        Foreign Key to Weapon in DB
    weapon_(various):
        Modified stats associated with Weapon
    weapon_level:
        Level of current weapon
    weapon_rarity:
        Rarity of current weapon

    """

    class Meta:
        verbose_name_plural = 'Active Enemies'

    class Rarity(models.TextChoices):
        COMMON = 1, _('Common')
        UNCOMMON = 2, _('Uncommon')
        RARE = 3, _('Rare')
        EPIC = 4, _('Epic')
        MYTHIC = 5, _('Mythic')

    active_character = models.OneToOneField(ActiveCharacter,
                                            on_delete=models.CASCADE)
    enemy_id = models.ForeignKey(Codex, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name="enemy")
    enemy_hp = models.IntegerField(null=False, blank=False)
    enemy_attack = models.IntegerField(null=False, blank=False)
    enemy_defense = models.IntegerField(null=False, blank=False)
    enemy_speed = models.IntegerField(null=False, blank=False)
    enemy_level = models.IntegerField(null=False, blank=False)
    weapon_id = models.ForeignKey(Codex, null=False, blank=False,
                                  on_delete=models.CASCADE,
                                  related_name="enemy_weapon")
    weapon_hp = models.IntegerField(null=False, blank=False)
    weapon_attack = models.IntegerField(null=False, blank=False)
    weapon_defense = models.IntegerField(null=False, blank=False)
    weapon_speed = models.IntegerField(null=False, blank=False)
    weapon_level = models.IntegerField(null=False, blank=False, default=1)
    weapon_rarity = models.CharField(max_length=10, choices=Rarity.choices,
                                     default=Rarity.COMMON)

    def __str__(self):
        return f'''{self.enemy_id.name} -
                {self.active_character.user.username}'s Enemy'''
