from django.db import models
from django.utils.translation import gettext_lazy as _
from random import randint
from .functions import rarity_recursive, stat_modifier


class CodexQuerySet(models.QuerySet):
    """
    Codex Query Set
    -----------

    Codex Query Set for all variants
    of queries and their associated business
    logic.

    custom_filter:
        Used for filtering the full codex for any search
        parameters or filters requested by the user.

    hero_select:
        Used for generating list of heroes for the user
        to choose from. Creates default set of "False",
        and adds the current user's paid state (True/False)
        and allows the query to obtain any hero in the DB with
        values in the set (allowed_content)

    get_random:
        Used for obtaining a single random entry in the database.
        This obtains a queryset, filters by the required parameters,
        counts the length of the queryset, and extracts a random index
        from the queryset. This is used for random items, and random enemies.
    """

    def custom_filter(self, search_params, sort_params):
        return self.filter(**search_params).order_by(sort_params)

    def hero_select(self, paid):
        allowed_content = {False}
        allowed_content.add(paid)
        return self.filter(type="Hero", paid__in=allowed_content)

    def get_random(self, type, paid, level):
        allowed_content = {False}
        allowed_content.add(paid)
        self = self.filter(type=type,
                           paid__in=allowed_content,
                           min_level__lte=level)
        last = self.count() - 1
        index = randint(0, last)  # nosec
        return self[index]


class CodexManager(models.Manager):
    """
    Codex Manager
    -----------

    Codex Manager for calling the custom
    Codex Query Sets.
    """

    def get_queryset(self):
        return CodexQuerySet(self.model, using=self._db)

    def filter_queryset(self, search_params, sort_params):
        return (
                self.get_queryset().custom_filter(search_params, sort_params)
        )

    def hero_select(self, paid):
        return self.get_queryset().hero_select(paid)

    def get_random(self, type, paid=False, level=1):
        return self.get_queryset().get_random(type, paid, level)


class Codex(models.Model):
    """
    Codex Model
    -----------

    Model for all entries within the Codex:

    name = Entry Name
    alpha_name = Organised Name
    type = Choice of Enemy, Weapon, or Hero
    base_hp = Base Hit Points of entry
    base_attack = Base Speed of entry
    base_defense = Base Defense of entry
    base_speed = Base Speed of entry
    image = Image name of entry
    paid = Bool to confirm whether premium entry
    min_level = User's minimum level threshold.
    """

    class Meta:
        verbose_name_plural = 'Codex'

    class TypeChoices(models.TextChoices):
        ENEMY = 'Enemy', _('Enemy')
        WEAPON = 'Weapon', _('Weapon')
        HERO = 'Hero', _('Hero')

    name = models.CharField(max_length=100)
    alpha_name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=10, choices=TypeChoices.choices,
                            default=TypeChoices.ENEMY)
    base_hp = models.IntegerField(default=5)
    base_attack = models.IntegerField(default=5)
    base_defense = models.IntegerField(default=5)
    base_speed = models.IntegerField(default=5)
    image = models.ImageField(null=False, blank=False)
    paid = models.BooleanField(default=False)
    min_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)],
                                    null=True, blank=True)
    objects = CodexManager()

    def __str__(self):
        return self.name

    @classmethod
    def new_weapon(cls, paid, level):
        """
        Method for generating a new weapon.

        Method takes in Paid Status and User Level.

        Level of the weapon is detemined at random,
        along with the rarity of the weapon.

        The base stats of the weapon generated are then
        modified by a random amount, the limits of the
        multiplier are effected by the weapon's current
        level and rarity.

        The stat modifications are applied by a order of
        magnitute equivalent to the weapon's rarity.
        """
        # Obtain new weapon
        weapon = cls.objects.get_random("Weapon", paid, level)

        # Determine level and rarity
        if level > 1:
            weapon.level = randint(1, level)  # nosec
            weapon.rarity = rarity_recursive(weapon.level)
        else:
            weapon.level = 1
            weapon.rarity = 1

        rarity_list = ["Common", "Uncommon", "Rare", "Epic", "Mythic"]
        weapon.rarity_text = rarity_list[weapon.rarity-1]

        # Apply modification in order of magnitude (rarity)
        for i in range(weapon.rarity):

            # Modify stats based on level and rarity
            weapon.base_hp = stat_modifier(weapon.base_hp,
                                           weapon.level,
                                           weapon.rarity)
            weapon.base_attack = stat_modifier(weapon.base_attack,
                                               weapon.level,
                                               weapon.rarity)
            weapon.base_speed = stat_modifier(weapon.base_speed,
                                              weapon.level,
                                              weapon.rarity)
            weapon.base_defense = stat_modifier(weapon.base_defense,
                                                weapon.level,
                                                weapon.rarity)
        return weapon

    @classmethod
    def new_enemy(cls, paid, level):
        """
        Method for generating a new enemy.

        Method takes in Paid Status and User Level.

        Level of the Enemy is detemined at random.

        The base stats of the enemy generated are modified
        n number of times, where n is the monster's level, based
        on the current monster's level.

        Enemy must be over level 1 for the modification to occur.
        """

        # Obtain new enemy
        enemy = cls.objects.get_random("Enemy", paid, level)
        # Determine level
        if level > 1:
            enemy.level = randint(1, level)  # nosec
            # Modify stats based on level (progressive)
            for i in range(enemy.level - 1):
                enemy.base_hp = stat_modifier(enemy.base_hp,
                                              enemy.level)
                enemy.base_attack = stat_modifier(enemy.base_attack,
                                                  enemy.level)
                enemy.base_speed = stat_modifier(enemy.base_speed,
                                                 enemy.level)
                enemy.base_defense = stat_modifier(enemy.base_defense,
                                                   enemy.level)
        else:
            enemy.level = 1
        return enemy
