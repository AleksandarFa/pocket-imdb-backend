from rest_framework.routers import SimpleRouter

from .views import MoviesViewset, GenreViewset, LikeViewset

movies_router = SimpleRouter()
movies_router.register(r'movies', MoviesViewset)
movies_router.register(r'genres', GenreViewset)
movies_router.register(r'likes', LikeViewset)
