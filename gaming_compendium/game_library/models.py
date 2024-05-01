from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]


class Platform(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='platform_name_case_insensitive_unique',
                violation_error_message = "Platform already exists (case insensitive match)"
            ),
        ]


class Game(models.Model):
    class Players(models.TextChoices):
        single = "Singleplayer", "Singleplayer"
        multiple = "Multiplayer", "Multiplayer"
        both = "Both", "Both"

    title = models.CharField(max_length = 100, primary_key = True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    platform = models.ManyToManyField(Platform)
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    player = models.CharField(max_length = 20, choices = Players.choices, default = Players.single)
    is_complete = models.BooleanField()
    time_to_beat = models.TextField()
    number = models.PositiveIntegerField(null = True, unique = True)

    def __str__(self):
        return self.title


class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
