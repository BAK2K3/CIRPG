"""
Leaderboard App - Views
----------------

Views for Leaderboard App.
    - LeaderboardView
"""

# pylint: disable=r0901

from django.views.generic import ListView
from .models import Leaderboard


class LeaderboardView(ListView):
    """
    A View for the Leaderboard Page.

    This view presents the top ten scored to the user.
    """
    model = Leaderboard
    template_name = 'leaderboard/leaderboard.html'
    context_object_name = 'leaderboard'

    def get_queryset(self):
        """Override get_queryset to sort the leaderboard entries"""
        return self.model.objects.sort_leaderboard()
