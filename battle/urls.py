"""
Battle App - URLS
---------------

URL Routing for the Battle App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BattleView.as_view(), name='battle'),
]
