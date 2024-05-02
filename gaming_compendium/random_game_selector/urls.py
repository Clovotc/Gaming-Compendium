from django.urls import path
from random_game_selector import views

urlpatterns = [
    path('', views.RandomGameView, name = 'randomgame'),
    path('randomselected/', views.RandomGameSelectedView, name = 'randomgameselected'),
]
