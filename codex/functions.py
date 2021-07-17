from random import randint, randrange
import math


# Function for processing GET kwargs
def process_codex_url(get_params):

    # Set default context dict
    context = {
            'premium': None,
            'entry_type': None,
            'levels': None,
            'search_params': {},
            'sort_by': 'pk',
            'sort_dir': None,
            'sort_params': 'pk',
        }

    # If sort criteria has been specified
    if 'sort' in get_params:
        if get_params['sort'] in ['name', 'type', 'base_hp',
                                  'base_attack', 'base_defense',
                                  'base_speed']:
            context['sort_by'] = get_params['sort']
            context['sort_params'] = context['sort_by']

    # If sort direction has been specified
    if 'direction' in get_params:
        if get_params['direction'] == 'desc':
            context['sort_dir'] = get_params['direction']
            context['sort_params'] = f"-{context['sort_by']}"

    # If Premium filter has been applied
    if 'premium' in get_params:
        if get_params['premium'] in ['0', '1']:
            context['premium'] = bool(int(get_params['premium']))
            context['search_params']['paid__exact'] = context['premium']

    # If Type filter has been applied
    if 'type' in get_params:
        if get_params['type'] in ['weapon', 'enemy', 'hero']:
            type_arg = get_params['type']
            context['entry_type'] = type_arg
            context['search_params']['type__icontains'] = type_arg

    # If min_level filter has been applied, and not hero type
    if 'levels' in get_params and context['entry_type'] != "hero":
        try:
            level_arg = [int(x) for x in get_params['levels'].split(',')]
            context['levels'] = level_arg
            context['search_params']['min_level__in'] = level_arg
        except ValueError as e:
            print(e)

    return context


def rarity_recursive(n, t=1):
    """
    Recursive Function to determine the grade of weapon

    1: Uncommon
    2: Common
    3: Rare
    4: Legendary
    5: Mythical

    Highest grade of weapon is determined by item level (max 5)
    Grade is determined by successive successful rolls
    Threshold for grades varies depending on item level.
    """

    # Determines success rate for this roll
    successroll = 100 - ((n - 1) * 20)

    # If success rate is 100%, return the current grade
    if successroll == 100 or t == 5:
        return t

    # Else, generate a random number between 1 and 100,
    else:
        outcome = randint(1, 100)  # nosec
        # If this roll is successful, increase weapon grade,
        # and recall function based on new thresholds
        if outcome >= successroll:
            return rarity_recursive((n - 1), t + 1)
        # If this roll is unsuccessful, return current grade
        else:
            return t


# Modifier Calculation
def modifier_multiplier(item_level, item_rarity=1):

    # Creates a minimum modifier
    modi_min = round((1 + ((item_level - 1) / 5)) * 100)
    # Creates a maximum modifier
    modi_max = round((1 + ((item_level - 1) / 5) + (item_rarity / 5)) * 100)
    # Creates a random number between min max
    multiplier = randrange(modi_min, modi_max) / 100  # nosec

    return multiplier


def stat_modifier(stat, level, rarity=1):
    return math.ceil(stat * modifier_multiplier(level, rarity))
