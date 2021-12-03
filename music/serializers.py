from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Song, Genre, Artist, User, Playlist


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(
            username=self.validated_data['username'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


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
        fields = ('id', 'title', 'artists', 'artwork', 'url', 'genres', 'views', 'duration', 'description')


class SongSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artists', 'artwork', 'url', 'genres', 'views', 'duration', 'description')


class ArtistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'information')


class FavoriteListSerializer(serializers.Serializer):
    songId = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)


class GenreSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'artwork')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'artwork')


class PlayListSongSerializer(serializers.Serializer):
    songId = serializers.IntegerField(required=True)
    playlist = serializers.CharField(required=True)

