from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from rest_framework import mixins, viewsets


class MoviesViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_fields = ['genre']
    search_fields = ['title']

class GenreViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
