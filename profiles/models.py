from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from codex.models import Codex


class Profile(models.Model):
    """
    Profile Model
    -----------

    Model for all User Profiles:

    user = Link to User model
    paid = Bool to represent paid user
    active_char = Bool to represent whether has an active char
    active_battle = Bool to represent whether user is in a battle
    total_runs = Int to represent total game attempts
    longest_run = Int to represent single high score

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    active_char = models.BooleanField(default=False)
    active_battle = models.BooleanField(default=False)
    total_runs = models.IntegerField(default=0)
    longest_run = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class ActiveCharacter(models.Model):

    """
    Active Characters Model
    -----------

    Model for all User Profiles:

    user = Link to User model
    paid = Bool to represent paid user
    active_char = Bool to represent whether has an active char
    active_battle = Bool to represent whether user is in a battle
    total_runs = Int to represent total game attempts
    longest_run = Int to represent single high score

    """

    class Meta:
        verbose_name_plural = 'Active Characters'

    class Rarity(models.TextChoices):
        COMMON = 1, _('Common')
        UNCOMMON = 2, _('Uncommon')
        RARE = 3, _('Rare')
        EPIC = 4, _('Epic')
        MYTHIC = 5, _('Mythic')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)],
                                        default=1)
    current_xp = models.IntegerField(default=0)
    battle_count = models.IntegerField(default=0)
    character_id = models.ForeignKey(Codex, null=False, blank=False,
                                     on_delete=models.CASCADE,
                                     related_name="character")
    char_hp = models.IntegerField(null=False, blank=False)
    char_attack = models.IntegerField(null=False, blank=False)
    char_defense = models.IntegerField(null=False, blank=False)
    char_speed = models.IntegerField(null=False, blank=False)
    weapon_id = models.ForeignKey(Codex, null=False, blank=False,
                                  on_delete=models.CASCADE,
                                  related_name="weapon")
    weapon_hp = models.IntegerField(null=False, blank=False)
    weapon_attack = models.IntegerField(null=False, blank=False)
    weapon_defense = models.IntegerField(null=False, blank=False)
    weapon_speed = models.IntegerField(null=False, blank=False)
    weapon_level = models.IntegerField(null=False, blank=False)
    weapon_rarity = models.CharField(max_length=10, choices=Rarity.choices,
                                     default=Rarity.COMMON)
