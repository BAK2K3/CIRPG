from django.shortcuts import render
from django.views.generic import TemplateView


class LeaderboardView(TemplateView):
    """
    A View for the Leaderboard Page.

    This view presents the top ten scored to the user.
    """
    template_name = 'leaderboard/leaderboard.html'
