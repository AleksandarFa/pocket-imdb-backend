from django.db import models
from src.users.models import User
from src.movies.models import Movie


class MovieComment(models.Model):
    comment = models.TextField(max_length=500, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
