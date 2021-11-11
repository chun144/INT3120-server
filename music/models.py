from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    information = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist, through='SongArtist')
    artwork = models.CharField(max_length=255, default=None)
    url_player = models.CharField(max_length=255, default=None)
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=50, default=None)
    genres = models.ManyToManyField(Genre, through='SongGenre')
    album = models.CharField(max_length=50, default=None)

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
