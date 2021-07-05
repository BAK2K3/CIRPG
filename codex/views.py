from django.shortcuts import render
from .models import Codex


def codex(request):
    """
    A view to return and filter all entries within codex.
    """
    # Query DB for codex entries
    codex = Codex.objects.all()

    # Initialise Filter Params
    premium = None
    entry_type = None
    levels = None
    search_params = {}

    if request.GET:
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

        # If any search parameters exist, apply the filter
        if len(search_params) > 0:
            codex = codex.filter(**search_params)

    # Add all queries to context
    context = {
        'codex': codex,
        'premium': premium,
        'entry_type': entry_type,
        'levels': levels
    }
    template = 'codex/codex.html'
    return render(request, template, context)
