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

    # Override get_queryset
    def get_queryset(self):
        # Obtain sorted leaderboard
        return self.model.objects.sort_leaderboard()
