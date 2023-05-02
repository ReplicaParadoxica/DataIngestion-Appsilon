from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=255)
    imdb_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Movie {self.id}"
