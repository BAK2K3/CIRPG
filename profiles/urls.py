"""
Profile App - URLS
---------------

URL Routing for the Profile App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile'),
]
