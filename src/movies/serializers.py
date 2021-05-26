from rest_framework import serializers
from .models import Movie, Genre, Like

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    num_of_likes = serializers.SerializerMethodField()
    num_of_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'genre', 'coverImage', 'num_of_likes', 'num_of_dislikes')

    def get_num_of_likes(self, obj):
        return Like.objects.filter(movie_id=obj.id).filter(liked=True).count()

    def get_num_of_dislikes(self, obj):
        return Like.objects.filter(movie_id=obj.id).filter(liked=False).count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
