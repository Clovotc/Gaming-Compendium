from django.shortcuts import render

# Create your views here.
def RandomGameView(request):
    
    return render(request, "random_game_selector/RandomGameView.html")

def RandomGameSelectedView(request):
    
    return render(request, "random_game_selector/RandomGameSelectedView.html")