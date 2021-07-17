from django.db import models
from codex.models import Codex
from profiles.models import ActiveCharacter, Profile
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
    enemy_level = models.IntegerField(null=False, blank=False, default=1)
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

    @classmethod
    def create_active_enemy(cls, user_profile):
        """
        Class method for creating a new active enemy.

        Takes in current user_profile.

        Queries DB for random enemy and weapon based on
        user's premium status and current char level.
        Creates an Active Enemy object before saving it to
        the database, and updating the current profile to confirm
        user has an active enemy.
        """

        active_character = ActiveCharacter.objects.get(user=user_profile.user)

        # Initialise dict and set user
        new_enemy = {}
        new_enemy["active_character"] = active_character

        # Query DB for selected user and assign to dict
        enemy = Codex.new_enemy(paid=user_profile.paid,
                                level=active_character.current_level)

        # Insert function here for stat modification
        new_enemy["enemy_id"] = enemy
        new_enemy["enemy_hp"] = enemy.base_hp
        new_enemy["enemy_attack"] = enemy.base_attack
        new_enemy["enemy_defense"] = enemy.base_defense
        new_enemy["enemy_speed"] = enemy.base_speed
        new_enemy["enemy_level"] = enemy.level

        # Obtain random  weapon from DB and assign to dict
        new_weapon = Codex.new_weapon(user_profile.paid,
                                      active_character.current_level)

        new_enemy["weapon_id"] = new_weapon
        new_enemy["weapon_hp"] = new_weapon.base_hp
        new_enemy["weapon_attack"] = new_weapon.base_attack
        new_enemy["weapon_defense"] = new_weapon.base_defense
        new_enemy["weapon_speed"] = new_weapon.base_speed
        new_enemy["weapon_level"] = new_weapon.level
        new_enemy["weapon_rarity"] = new_weapon.rarity

        # Create ActiveCharacter object and save
        entry = cls(**new_enemy)
        entry.save()

        # Update user profile to reflect new character
        user_profile = Profile.objects.get(user=user_profile.user)
        user_profile.active_battle = True
        user_profile.save()

        return entry
