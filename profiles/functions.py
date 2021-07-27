from codex.functions import stat_modifier
from codex.models import Codex
from random import randint


def calculate_xp(character, enemy_level):
    """
    Function for calculating XP Gain

    Takes in character object and enemy_level.
    Updates character XP gain and thresholds.
    Returns True if character levels up.
    """

    # Calculate XP Gained and add to character
    current_level = character.current_level
    potential_xp = round((enemy_level / current_level) * 100)
    character.current_xp += potential_xp
    character.battle_count += 1

    # Determine whether user has levelled up
    if character.current_xp >= character.max_xp:

        # Set user's new level and XP thresholds
        character.current_level += 1
        character.min_xp = (100 * ((character.current_level - 1) ** 2)) + 100
        character.max_xp = (100 * (character.current_level ** 2)) + 100

        # Randomly add up to 1 metric to each stat:
        character.char_hp += 5 * randint(0, 1)  # nosec
        character.char_attack += 1 * randint(0, 1)  # nosec
        character.char_speed += 1 * randint(0, 1)  # nosec
        character.char_defense += 1 * randint(0, 1)  # nosec

        # Further upgrade users stats using stat modifier
        character.char_hp = stat_modifier(character.char_hp,
                                          character.current_level)
        character.char_attack = stat_modifier(character.char_attack,
                                              character.current_level)
        character.char_speed = stat_modifier(character.char_speed,
                                             character.current_level)
        character.char_defense = stat_modifier(character.char_defense,
                                               character.current_level)
        character.save()
        return True

    character.save()
    return False


def add_weapon(character, weapon_dict):
    """
    Function for taking in existing "Active Character" instance
    and modified weapon dictionary, and updating the required
    fields of the "Active Character" instance to reflect users
    request to update current weapon.

    Function takes in character that needs modifying,
    and weapon_dict of the requested weapon.
    """
    weapon_model = Codex.objects.get(pk=weapon_dict['id'])

    character.weapon_id = weapon_model
    character.weapon_hp = weapon_dict['base_hp']
    character.weapon_attack = weapon_dict['base_attack']
    character.weapon_defense = weapon_dict['base_defense']
    character.weapon_speed = weapon_dict['base_speed']
    character.weapon_level = weapon_dict['level']
    character.weapon_rarity = weapon_dict['rarity']
    character.save()
