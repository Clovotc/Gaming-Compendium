from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length = 100, primary_key = True)
    game_description = models.TextField()
    game_genre = models.CharField(max_length = 50)
    game_rating = models.CharField(max_length = 50)
    game_completed = models.BooleanField()
    time_to_beat = models.TextField()

    def __str__(self):
        return self.game_name
