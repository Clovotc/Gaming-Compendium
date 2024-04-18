from django.urls import path
from game_library import views

urlpatterns = [
    path('', views.index, name='games'),
]
