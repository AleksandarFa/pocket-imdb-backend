from .models import Movie
from .serializers import MovieSerializer
from rest_framework import mixins, viewsets


# Create your views here.
class MoviesViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
