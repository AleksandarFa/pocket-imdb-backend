from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from rest_framework import mixins, viewsets


class MoviesViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
