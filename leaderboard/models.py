"""
Leaderboard App - Models
----------------

Models for Leaderboard App.
    - LeaderboardQuerySet
    - LeaderboardManager
    - Leaderboard
"""

# pylint: disable=E5142

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from codex.models import Codex


class LeaderboardQuerySet(models.QuerySet):
    """
    Leaderboard Query Set
    -----------

    Leaderboard Query Set for all variants
    of queries and their associated business
    logic.

    sort_leaderboard:
        Used for sorting the Leaderboard entry in order
        of descending score.
    """

    def sort_leaderboard(self):
        """Sorts query by score in descending order."""
        return self.order_by("-score")


class LeaderboardManager(models.Manager):
    """
    Leaderboard Manager
    -----------

    Leaderboard Manager for calling the custom
    Leaderboard Query Sets.

    get_queryset:
        Overrides the default Model Manager Get Queryset
        to utilise the LeaderboardQuerySet.

    sort_leaderboard:
        Calls the sort_leaderboard queryset.

    """

    def get_queryset(self):
        """
        Overrides the default Model Manager Get Queryset
        to utilise the LeaderboardQuerySet.
        """
        return LeaderboardQuerySet(self.model, using=self._db)

    def sort_leaderboard(self):
        """Calls the sort_leaderboard queryset."""
        return self.get_queryset().sort_leaderboard()


class Leaderboard(models.Model):
    """
    Leaderboard Model
    -----------

    Model for Leaderboard entries.
    Designed to only contain top 10 scores.
    Score is calculated as follows:

    All stats combined + level + number of runs + xp.

    Attributes
    ----------

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

    Methods
    -------

    active_char_to_leaderboard:
        Creates a leaderboard entry and saves it to the database

    calculate_score:
        Calculates the score of an active player.

    leaderboard_check:
        Checks whether active character has earned a place on the scoreboard

    """

    class Meta:
        verbose_name_plural = 'Leaderboard'

    class Rarity(models.TextChoices):
        """Rarity Text Choices for model Type field"""
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
    objects = LeaderboardManager()

    def __str__(self):
        return f'{self.user.username} | Score {self.score } '

    @classmethod
    def active_char_to_leaderboard(cls, active_char, score):
        """
        Class method for building the required structure of
        the leaderboard model before saving it to the database.

        Method takes in active character and their score.
        """

        entry = {}
        entry['user'] = active_char.user
        entry['current_level'] = active_char.current_level
        entry['battle_count'] = active_char.battle_count
        entry['character_id'] = active_char.character_id
        entry['char_hp'] = active_char.char_hp
        entry['char_attack'] = active_char.char_attack
        entry['char_defense'] = active_char.char_defense
        entry['char_speed'] = active_char.char_speed
        entry['weapon_id'] = active_char.weapon_id
        entry['weapon_hp'] = active_char.weapon_hp
        entry['weapon_attack'] = active_char.weapon_attack
        entry['weapon_defense'] = active_char.weapon_defense
        entry['weapon_speed'] = active_char.weapon_speed
        entry['weapon_level'] = active_char.weapon_level
        entry['weapon_rarity'] = active_char.weapon_rarity
        entry['score'] = score

        new_leaderboard_entry = cls(**entry)
        new_leaderboard_entry.save()

    @staticmethod
    def calculate_score(active_char):
        """
        Static method for calculating the score of an active
        player. Used for comparing entries within the database,
        and for saving new entry to the DB.
        """
        score = 0
        score += active_char.current_level
        score += active_char.battle_count
        score += active_char.current_xp
        score += active_char.char_hp
        score += active_char.char_attack
        score += active_char.char_speed
        score += active_char.char_defense
        score += active_char.weapon_hp
        score += active_char.weapon_attack
        score += active_char.weapon_speed
        score += active_char.weapon_defense
        score += active_char.weapon_level
        return score

    @classmethod
    def leaderboard_check(cls, active_char):
        """
        Class method for checking whether active character
        has earned a place on the scoreboard.

        Method obtains all current entries in leaderboard
        DB, calculates users score, and determines whether
        the active characters score is higher than the lowest
        entry in the DB. If so, or if there are less than 10
        entries in the DB, the method calls the active_char_to_leaderboard
        method to store the active character and their score to the DB.

        Returns Bool to confirm if score has been entered, and players score.
        """

        current_leaderboard = cls.objects.sort_leaderboard()
        score = cls.calculate_score(active_char)

        if len(current_leaderboard) >= 10:
            if current_leaderboard[9].score > score:
                return (False, score)
            current_leaderboard[9].delete()
            cls.active_char_to_leaderboard(active_char, score)
            return (True, score)
        cls.active_char_to_leaderboard(active_char, score)
        return (True, score)
