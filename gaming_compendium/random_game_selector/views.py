from django.shortcuts import render
from game_library.models import Game
import random
# Create your views here.

def RandomGameView(request):
    
    return render(request, "random_game_selector/RandomGameView.html")

def RandomGameSelectedView(request):


    ran = random.randint(1,50)
    random_game = Game.objects.filter(number=ran).values_list('title', flat = True)
    random_game_string = str(random_game)
    random_game_string = random_game_string[12:-3]
    formatted_random_game_string=random_game_string
    random_game_image = "/static/random_game_selector/images/{}.jpg".format(formatted_random_game_string) 
    random_game_image_url = random_game_image.replace(" ", "_")

    context = {
        "formatted_random_game_string": formatted_random_game_string,
        "random_game_image_url": random_game_image_url,
    }

    return render(request, "random_game_selector/RandomGameSelectedView.html", context)
 