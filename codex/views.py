from django.shortcuts import render
from .models import Codex


def codex(request):
    """
    A view to return all entries within codex.
    """
    codex = Codex.objects.all()
    context = {
        'codex': codex
    }
    return render(request, 'codex/codex.html', context)
