"""
Leaderboard App - URLS
---------------

URL Routing for the Leaderboard App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeaderboardView.as_view(), name='leaderboard'),
]
