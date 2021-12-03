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
    information = models.CharField(max_length=1000, default='N/A')

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=50)
    artwork = models.CharField(max_length=255, default='https://res.cloudinary.com/dwc4kzyds/image/upload/v1637651180/Data/Default/logo_mjrwxc.png')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    artwork = models.CharField(max_length=255, default='https://res.cloudinary.com/dwc4kzyds/image/upload/v1637651180/Data/Default/logo_mjrwxc.png')

    class Meta:
        unique_together = [['title']]

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist, through='SongArtist')
    artwork = models.CharField(max_length=255, default='https://res.cloudinary.com/dwc4kzyds/image/upload/v1637651180/Data/Default/logo_mjrwxc.png')
    url = models.CharField(max_length=255, default='N/A')
    views = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre, through='SongGenre')
    description = models.CharField(max_length=1000, default='N/A')

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


class FavoriteList(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['song', 'user']]


class SongPlaylist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['song', 'playlist']]
