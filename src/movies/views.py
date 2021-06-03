from src.files.models import File
from .models import Movie, Genre, Like
from .serializers import MovieSerializer, GenreSerializer, LikeSerializer, WatchListSerializer, CreateMovieSerializer
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework import status

# from django.core.mail import mail_admins


class MoviesViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializers = {
        'default': MovieSerializer,
        'create_movie': CreateMovieSerializer,
        'watch_list': WatchListSerializer
    }

    filterset_fields = ['genre']
    search_fields = ['title']
    ordering_fields = ['like']

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

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

    @action(detail=False, methods=["POST"])
    def create_movie(self, request):
        serializer_class = self.get_serializer_class()
        movie = serializer_class(data=request.data)
        movie.is_valid(raise_exception=True)
        genre = movie.validated_data.pop('genre')
        genreObj = Genre.objects.filter(name=genre["name"])[0]

        cover_image = movie.validated_data.pop('cover_image')
        cover_image_obj = File.objects.filter(id=cover_image)[0]

        Movie.objects.create(genre=genreObj, cover_image=cover_image_obj, **movie.validated_data)
        return Response(movie.validated_data, status=status.HTTP_201_CREATED)

    @action(detail=False, pagination_class=None, methods=['GET', 'POST', 'PUT', 'DELETE'])
    def watch_list(self, request):
        serializer_class = self.get_serializer_class()
        if request.method == 'GET':
            queryset = Movie.watch_list.through.objects.all().filter(user_id=request.user.id)
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data.update({'user': serializer.validated_data['user'].id})
            movie = Movie.objects.get(id=serializer.validated_data['movie']["id"])

            if request.method == "POST":
                movie.watch_list.add(serializer.validated_data["user"], through_defaults={
                                     'watched': serializer.validated_data['watched']})
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            elif request.method == "PUT":
                watch_list_item = Movie.watch_list.through.objects.filter(movie=movie.id, user=request.user.id)[0]
                watch_list_item.watched = serializer.validated_data['watched']
                watch_list_item.save()
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            elif request.method == "DELETE":
                movie.watch_list.remove(request.user)
                return Response(serializer.validated_data, status=status.HTTP_200_OK)


class GenreViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class LikeViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    ordering_fields = ['like']
