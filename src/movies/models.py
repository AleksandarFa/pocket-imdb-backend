from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from ..files.models import File
from ..users.models import User
from ..common.tasks import send_email_task

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


@receiver(post_save, sender=Movie)
def handle_email(sender, instance, created, **kwargs):
    if created:
        message = "Movie : {} is successfully created.".format(instance.title)
        send_email_task.delay("Movie creation", ["aleksandar.fa@vivifyideas.com"], "no@replay.com", message)
