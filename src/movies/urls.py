from rest_framework.routers import SimpleRouter

from .views import MoviesViewset

movies_router = SimpleRouter()
movies_router.register(r'movies', MoviesViewset)
