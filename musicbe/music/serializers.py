from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'cover', 'url_player', 'views', 'duration', 'genre', 'album')
