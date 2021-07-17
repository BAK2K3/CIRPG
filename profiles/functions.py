from codex.functions import stat_modifier


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

    # Determine whether user has levelled up
    if character.current_xp >= character.max_xp:

        # Set user's new level and XP thresholds
        character.current_level += 1
        character.min_xp = (100 * ((current_level - 1) ** 2)) + 100
        character.max_xp = (100 * (current_level ** 2)) + 100

        # Upgrades users stats
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
