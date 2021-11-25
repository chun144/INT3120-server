from django.contrib import admin
from .models import Song, Genre, SongGenre, Artist, SongArtist, User, FavoriteList

# Register your models here.
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(SongGenre)
admin.site.register(SongArtist)
admin.site.register(User)
admin.site.register(FavoriteList)
