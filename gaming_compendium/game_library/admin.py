from django.contrib import admin
from game_library.models import Game, Genre, Developer, Platform

# Register your models here.

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Platform)
