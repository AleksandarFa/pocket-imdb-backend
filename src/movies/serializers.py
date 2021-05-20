from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'genre', 'coverImage')
