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
    path('checkout/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view(), name="success"),
    path('abort/', views.AbortView.as_view(), name="abort"),
    path('webhook/', views.stripe_webhook),
]
