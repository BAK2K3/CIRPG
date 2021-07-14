"""
Profile App - URLS
---------------

URL Routing for the Profile App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile'),
    path('create/', views.CreateHeroDetailView.as_view(), name='create'),
    path('create_submit/',
         views.CreateHeroFormView.as_view(),
         name='create_submit')
]
