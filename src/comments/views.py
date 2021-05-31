from rest_framework import viewsets
from .models import MovieComment
from .serializers import MovieCommentSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer
    filterset_fields = ['movie']
