"""
Codex App - URLS
---------------

URL Routing for the Codex App
"""

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'$', views.CodexListView.as_view(), name='codex'),
]
