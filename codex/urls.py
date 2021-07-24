"""
Codex App - URLS
---------------

URL Routing for the Codex App
"""

from django.urls import re_path, path
from . import views

urlpatterns = [
    path('delete/<slug:pk>/',
         views.CodexDeleteView.as_view(),
         name='c_delete'),
    path('edit/<slug:pk>/', views.CodexUpdateView.as_view(), name='c_edit'),
    path('create/', views.CodexCreateView.as_view(), name='c_create'),
    re_path(r'$', views.CodexListView.as_view(), name='codex')
]
