from rest_framework import serializers
from .models import Genre, Developer, VideoGame, GameDeveloper
from django.conf import settings

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class VideoGameSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = VideoGame
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        video_game = super().create(validated_data)
        if image:
            video_game.cover_image_url = self.save_image(video_game, image)
            video_game.save()
        return video_game

    def save_image(self, video_game, image):
        from django.core.files.storage import default_storage 
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('images', str(video_game.id) + '_' + image.
        name), ContentFile(image.read())) 
        return settings.MEDIA_URL + path

class GameDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDeveloper
        fields = '__all__'