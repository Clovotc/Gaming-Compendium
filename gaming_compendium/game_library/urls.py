from django.urls import path
from game_library import views
from random_game_selector import views as random_views

urlpatterns = [
    path('', views.index, name='games'),
    path('random/', random_views.RandomGameView, name = 'randomgame'),
    path('random/randomselected/', random_views.RandomGameSelectedView, name = 'randomgameselected'),
]
