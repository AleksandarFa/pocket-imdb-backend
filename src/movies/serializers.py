from rest_framework import serializers
from .models import Movie, Genre, Like, WatchList


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    num_of_likes = serializers.SerializerMethodField()
    num_of_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        extra_kwargs = {'id': {'read_only': False}}

    def get_num_of_likes(self, obj):
        return Like.objects.filter(movie_id=obj.id).filter(liked=True).count()

    def get_num_of_dislikes(self, obj):
        return Like.objects.filter(movie_id=obj.id).filter(liked=False).count()


class CreateMovieSerializer(MovieSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = WatchList
        fields = "__all__"
