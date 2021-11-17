from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Delete not use field
    last_login = None

    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Artist(models.Model):
    name = models.CharField(max_length=50)
    information = models.CharField(max_length=255, default='No information available')

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist, through='SongArtist')
    artwork = models.CharField(max_length=255, default='https://res.cloudinary.com/dwc4kzyds/image/upload/v1636832140/Image/logo.png')
    url_player = models.CharField(max_length=255, default='null')
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=50, default='null')
    genres = models.ManyToManyField(Genre, through='SongGenre')
    album = models.CharField(max_length=50, default='null')

    def __str__(self):
        return self.title


class SongGenre(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['song', 'genre']]


class SongArtist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['song', 'artist']]
