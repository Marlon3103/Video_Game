from django.urls import include, path
from rest_framework import routers
from .views import GenreViewSet, DeveloperViewSet, VideoGameViewSet, GameDeveloperViewSet

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'developers', DeveloperViewSet)
router.register(r'video-games', VideoGameViewSet)
router.register(r'game-developers', GameDeveloperViewSet)

urlpatterns = [
    path("api/v1/", include (router.urls))
]
