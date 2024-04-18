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


class Game(models.Model):
    title = models.CharField(max_length = 100, primary_key = True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    is_complete = models.BooleanField()
    time_to_beat = models.TextField()

    def __str__(self):
        return self.title


class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
