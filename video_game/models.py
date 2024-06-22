from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

class Developer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

class VideoGame(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    cover_image_url = models.URLField(max_length=255, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class GameDeveloper(models.Model):
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
