from rest_framework import serializers
from .models import MovieComment

class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = "__all__"
