from django.contrib import admin
from game_library.models import Game, Genre, Developer

# Register your models here.

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
