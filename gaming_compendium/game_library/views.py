from django.shortcuts import render
from game_library.models import Game

# Create your views here.

def index(request):
    game_list = Game.objects.all()
    return render(request, 'game_library/index.html', {'game_list': game_list})
