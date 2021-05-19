from django.db import models
from ..files.models import File

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    coverImage = models.ForeignKey(File, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.CharField(max_length=8, choices=[("SCI-FI", "Sci-fi"), ("DRAMA", "Drama"), ("THRILLER", "Thriller"),
                             ("HORROR", "Horror"), ("COMEDY", "Comedy"), ("ACTION", "Action")], default="ACTION")

    def __str__(self):
        return self.title
