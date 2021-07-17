"""
Battle App - URLS
---------------

URL Routing for the Battle App
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BattleView.as_view(), name='battle'),
    path('post_battle/', views.PostBattleView.as_view(), name='post_battle'),
    path('loot/', views.NewLootView.as_view(), name='loot')
]
