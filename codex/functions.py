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
