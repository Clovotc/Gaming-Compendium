from django.shortcuts import render
from game_library.models import Game, Genre, Developer, Platform

# Create your views here.

def is_valid_query_param(param):
    return param != "" and param is not None


def index(request):
    game_list = Game.objects.all().order_by("title")
    genre_list = Genre.objects.all().order_by("name")
    developer_list = Developer.objects.all().order_by("name")
    platform_list = Platform.objects.all().order_by("name")

    title_contains_search = request.GET.get("title_contains")
    selected_genre = request.GET.get("genre")
    selected_developer = request.GET.get("developer")
    selected_platform = request.GET.get("platform")

    if  is_valid_query_param(title_contains_search):
        game_list = game_list.filter(title__icontains = title_contains_search)

    if is_valid_query_param(selected_genre) and selected_genre != 'Choose...':
        game_list = game_list.filter(genre__name = selected_genre)

    if is_valid_query_param(selected_developer) and selected_developer != 'Choose...':
        game_list = game_list.filter(developer__name = selected_developer)

    if is_valid_query_param(selected_platform) and selected_platform != 'Choose...':
        game_list = game_list.filter(platform__name = selected_platform)

    context = {"game_list": game_list, 
               "genre_list": genre_list, 
               "developer_list": developer_list, 
               "platform_list": platform_list,}
    
    return render(request, "game_library/index.html", context)
