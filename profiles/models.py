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

    @classmethod
    def remove_active_char(cls, user):
        current_user = cls.objects.get(user=user)
        current_user.active_char = False
        current_user.save()


class ActiveCharacter(models.Model):

    """
    Active Characters Model
    -----------

    Model for active characters.
    These can be removed by the user,
    or when a character dies.

    user:
        Associated User
    current_level:
        Level of current char
    current_xp:
        Experience determining Level
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
        verbose_name_plural = 'Active Characters'

    class Rarity(models.TextChoices):
        COMMON = 1, _('Common')
        UNCOMMON = 2, _('Uncommon')
        RARE = 3, _('Rare')
        EPIC = 4, _('Epic')
        MYTHIC = 5, _('Mythic')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_level = models.IntegerField(default=1)
    current_xp = models.IntegerField(default=0)
    min_xp = models.IntegerField(default=0)
    max_xp = models.IntegerField(default=200)
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
    weapon_level = models.IntegerField(null=False, blank=False, default=1)
    weapon_rarity = models.CharField(max_length=10, choices=Rarity.choices,
                                     default=Rarity.COMMON)

    def __str__(self):
        return f"{self.user.username} - Level {self.current_level}"

    @classmethod
    def create_character(cls, user, hero_name, paid):
        """
        Class method for creating a new active character.

        Takes in current user, chosen hero name, and paid status.

        Queries DB for chosen hero, generates a weapon, and then
        creates an Active Character object before saving it to
        the database, and updating the current profile to confirm
        user has an active character.
        """
        # Initialise dict and set user
        new_character = {}
        new_character["user"] = user

        # Query DB for selected user and assign to dict
        hero = Codex.objects.get(name=hero_name)
        new_character["character_id"] = hero
        new_character["char_hp"] = hero.base_hp
        new_character["char_attack"] = hero.base_attack
        new_character["char_defense"] = hero.base_defense
        new_character["char_speed"] = hero.base_speed

        # Obtain random starter weapon from DB and assign to dict
        new_weapon = Codex.new_weapon(paid, 1)

        new_character["weapon_id"] = new_weapon
        new_character["weapon_hp"] = new_weapon.base_hp
        new_character["weapon_attack"] = new_weapon.base_attack
        new_character["weapon_defense"] = new_weapon.base_defense
        new_character["weapon_speed"] = new_weapon.base_speed

        # Create ActiveCharacter object and save
        entry = cls(**new_character)
        entry.save()

        # Update user profile to reflect new character
        user_profile = Profile.objects.get(user=user)
        user_profile.active_char = True
        user_profile.save()

        return entry

    def update_character(self):
        pass

    def update_weapon(self, weapon):
        self.weapon_id = weapon.pk
        self.weapon_hp = weapon.base_hp
        self.weapon_attack = weapon.base_attack
        self.weapon_defense = weapon.base_defense
        self.weapon_speed = weapon.base_speed
        self.weapon_level = weapon.base_level
        self.weapon_rarity = weapon.base_rarity
        self.save()
