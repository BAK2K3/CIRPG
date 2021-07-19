"""
Premium App - URLS
---------------

URL Routing for the Home App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PremiumView.as_view(), name="premium"),
    path('config/', views.stripe_config),
]
