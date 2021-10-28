from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    cover = models.CharField(max_length=255, default=None)
    url_player = models.CharField(max_length=255, default=None)
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=50, default=None)
    genre = models.CharField(max_length=50, default=None)
    album = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.title
