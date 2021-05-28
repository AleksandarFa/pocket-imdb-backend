from django.contrib import admin
from .models import Movie, Genre, Like, WatchList

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Like)
admin.site.register(WatchList)
