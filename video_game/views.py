from rest_framework import viewsets, permissions
from .models import Genre, Developer, VideoGame, GameDeveloper
from .serializer import GenreSerializer, DeveloperSerializer, VideoGameSerializer, GameDeveloperSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class VideoGameViewSet(viewsets.ModelViewSet): 
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer

class GameDeveloperViewSet(viewsets.ModelViewSet): 
    serializer_class = GameDeveloperSerializer
    queryset = GameDeveloper.objects.all()