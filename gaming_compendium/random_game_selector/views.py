from django.shortcuts import render
from game_library.models import Game

# Create your views here.

def RandomGameView(request):
    
    return render(request, "random_game_selector/RandomGameView.html")

def RandomGameSelectedView(request):
    
    # random = Game.title

    # random_game = f"/static/random_game_selector/images/{random}.jpg"

    return render(request, "random_game_selector/RandomGameSelectedView.html")
