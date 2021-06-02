from django.db import models
from ..files.models import File
from ..users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ForeignKey(File, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    num_of_views = models.IntegerField(default=0)
    watch_list = models.ManyToManyField(User, through="WatchList")

    def __str__(self):
        return self.title


class Like(models.Model):
    liked = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'movie_id')


class WatchList(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
