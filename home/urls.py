"""
Home App - URLS
---------------

URL Routing for the Home App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
]
