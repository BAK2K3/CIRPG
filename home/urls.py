"""
Home App - URLS
---------------

URL Routing for the Home App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('help/', views.HelpView.as_view(), name="help"),
]
