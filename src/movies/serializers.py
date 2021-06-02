from rest_framework import serializers
from .models import Movie, Genre, Like, WatchList
from src.files.serializers import FileSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    cover_image = FileSerializer()
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
    cover_image = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class MovieWatchListSerializer(MovieSerializer):
    cover_image = FileSerializer(required=False)

    class Meta:
        model = Movie
        fields = "__all__"
        extra_kwargs = {'id': {'read_only': False}}


class WatchListSerializer(serializers.ModelSerializer):
    movie = MovieWatchListSerializer()

    class Meta:
        model = WatchList
        fields = "__all__"
