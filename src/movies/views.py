from .models import Movie, Genre, Like
from .serializers import MovieSerializer, GenreSerializer, LikeSerializer, WatchListSerializer
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework import status


class MoviesViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_fields = ['genre']
    search_fields = ['title']
    ordering_fields = ['like']

    def retrieve(self, request, pk):
        instance = self.get_object()
        instance.num_of_views += 1
        instance.save()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance)
        return Response(serializer.data)

    @action(detail=False, pagination_class=None)
    def popular(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        sortedData = sorted(serializer.data, key=lambda x: x['num_of_likes'], reverse=True)
        return Response(sortedData[:10])

    @action(detail=False, pagination_class=None, methods=['GET', 'POST', 'PUT', 'DELETE'])
    def watch_list(self, request):
        queryset = Movie.watch_list.through.objects.all().filter(user_id=request.user.id)
        serializer = WatchListSerializer(queryset, many=True)

        if request.method != 'GET':
            serializer = WatchListSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            movie = Movie.objects.get(id=serializer.data['movie'])

            if request.method == "POST":
                movie.watch_list.add(request.user, through_defaults={'watched': serializer.data['watched']})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif request.method == "PUT":
                watch_list_item = Movie.watch_list.through.objects.filter(movie=movie.id, user=request.user.id)[0]
                watch_list_item.watched = serializer.data['watched']
                watch_list_item.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.method == "DELETE":
                movie.watch_list.remove(request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)


class GenreViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class LikeViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    ordering_fields = ['like']
