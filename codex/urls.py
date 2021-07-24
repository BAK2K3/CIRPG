"""
Codex App - URLS
---------------

URL Routing for the Codex App
"""

from django.urls import re_path, path
from . import views

urlpatterns = [
    path('edit/<slug:pk>/', views.CodexUpdateView.as_view(), name='c_edit'),
    re_path(r'$', views.CodexListView.as_view(), name='codex')
]
