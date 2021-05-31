from rest_framework.routers import SimpleRouter
from .views import CommentViewset

comments_router = SimpleRouter()
comments_router.register(r'comments', CommentViewset)
