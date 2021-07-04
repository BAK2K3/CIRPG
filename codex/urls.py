"""
Codex App - URLS
---------------

URL Routing for the Codex App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.codex, name="codex"),
]
