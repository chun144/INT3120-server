from rest_framework import serializers

from .models import Song, Genre, Artist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title',)
        depth = 1


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)
        depth = 1


class SongSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Song
        fields = ('id', 'title', 'artists', 'artwork', 'url_player', 'genres', 'views', 'duration', 'album')


class SongSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artists', 'artwork', 'url_player', 'genres', 'views', 'duration', 'album')


class ArtistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'information')
