from django.contrib import admin
from .models import Song, Genre, SongGenre, Artist, SongArtist

# Register your models here.
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(SongGenre)
admin.site.register(SongArtist)
