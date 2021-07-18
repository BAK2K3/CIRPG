from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from codex.models import Codex


class Leaderboard(models.Model):
    """
    Leaderboard Model
    -----------

    Model for Leaderboard entries.
    Designed to only contain top 10 scores.
    Score is calculated as follows:

    All stats combined + level + number of runs + xp.

    user:
        Associated User
    submission_date:
        DateTime of leaderboard submission
    current_level:
        Level of Character
    current_xp:
        XP of character
    battle_count:
        Amount of successful battles
    character_id:
        Foreign Key to Hero in DB
    character_(various):
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
        verbose_name_plural = 'Leaderboard'

    class Rarity(models.TextChoices):
        COMMON = 1, _('Common')
        UNCOMMON = 2, _('Uncommon')
        RARE = 3, _('Rare')
        EPIC = 4, _('Epic')
        MYTHIC = 5, _('Mythic')

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=False, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=False, blank=False)
    current_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)],
                                        blank=False, null=False)
    battle_count = models.IntegerField(blank=False, null=False)
    character_id = models.ForeignKey(Codex, null=True, blank=False,
                                     on_delete=models.SET_NULL,
                                     related_name="leaderboard_character")
    char_hp = models.IntegerField(null=False, blank=False)
    char_attack = models.IntegerField(null=False, blank=False)
    char_defense = models.IntegerField(null=False, blank=False)
    char_speed = models.IntegerField(null=False, blank=False)
    weapon_id = models.ForeignKey(Codex, null=True, blank=False,
                                  on_delete=models.CASCADE,
                                  related_name="leaderboard_weapon")
    weapon_hp = models.IntegerField(null=False, blank=False)
    weapon_attack = models.IntegerField(null=False, blank=False)
    weapon_defense = models.IntegerField(null=False, blank=False)
    weapon_speed = models.IntegerField(null=False, blank=False)
    weapon_level = models.IntegerField(null=False, blank=False, default=1)
    weapon_rarity = models.CharField(max_length=10, choices=Rarity.choices,
                                     default=Rarity.COMMON, null=False,
                                     blank=False)

    def __str__(self):
        return (f'{self.user.username} | Score {self.score } ')
        