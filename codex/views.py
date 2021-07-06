from django.shortcuts import render
from .models import Codex


def codex(request):
    """
    A view to return all entries within codex.
    View takes parameters for both sorting and searching.
    These paremeters are then returned to the view for
    template logic.
    """
    # Query DB for codex entries
    codex = Codex.objects.all()

    # Initialise Sort/Filter Params
    premium = None
    entry_type = None
    levels = None
    search_params = {}
    sort_by = 'pk'
    sort_dir = None
    sort_params = sort_by

    if request.GET:
        # If sort criteria has been specified
        if 'sort' in request.GET:
            if request.GET['sort'] in ['name', 'type', 'base_hp',
                                       'base_attack', 'base_defense',
                                       'base_speed']:
                sort_by = request.GET['sort']
                sort_params = sort_by

        # If sort direction has been specified
        if 'direction' in request.GET:
            if request.GET['direction'] == 'desc':
                sort_dir = request.GET['direction']
                sort_params = f'-{sort_by}'

        # Perform sort functionality
        codex = codex.order_by(sort_params)

        # If Premium filter has been applied
        if 'premium' in request.GET:
            if request.GET['premium'] in ['0', '1']:
                premium = bool(int(request.GET['premium']))
                codex = codex.filter(paid__exact=premium)

        # If Type filter has been applied
        if 'type' in request.GET:
            if request.GET['type'] in ['weapon', 'enemy', 'hero']:
                entry_type = request.GET['type']
                search_params['type__icontains'] = entry_type

        # If min_level filter has been applied, and not hero type
        if 'levels' in request.GET and entry_type != "hero":
            try:
                levels = [int(x) for x in request.GET['levels'].split(',')]
                search_params['min_level__in'] = levels
            except ValueError as e:
                print(e)

        # If any filter parameters exist, apply the filter
        if len(search_params) > 0:
            codex = codex.filter(**search_params)

    # Add all queries to context
    context = {
        'codex': codex,
        'premium': premium,
        'entry_type': entry_type,
        'levels': levels,
        'sort_by': sort_by,
        'sort_dir': sort_dir,
    }
    template = 'codex/codex.html'
    return render(request, template, context)
