from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_review', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    score = models.IntegerField()
