from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Song, Genre, SongGenre, Artist, SongArtist
from .serializers import SongSerializer, SongSerializerPost


class ListCreateSongView(ListCreateAPIView):
    model = Song
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = SongSerializerPost(data=request.data)

        if serializer.is_valid():
            artists = request.data['artists']
            genres = request.data['genres']
            serializer.save()
            song = Song.objects.get(pk=serializer.data['id'])
            for i in genres:
                try:
                    genre = Genre.objects.get(title=i)
                except Genre.DoesNotExist:
                    genre = None
                if genre is None:
                    genre = Genre.objects.create(title=i)

                SongGenre.objects.create(song=song, genre=genre)

            for i in artists:
                try:
                    artist = Artist.objects.get(name=i)
                except Artist.DoesNotExist:
                    artist = None
                if artist is None:
                    artist = Artist.objects.create(name=i, information='No information available')

                SongArtist.objects.create(song=song, artist=artist)

            songNew = get_object_or_404(Song, id=serializer.data['id'])
            serializerSong = SongSerializer(songNew)
            return Response(data=serializerSong.data, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Create a new Song unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteSongView(RetrieveUpdateDestroyAPIView):
    model = Song
    serializer_class = SongSerializer

    def put(self, request, *args, **kwargs):
        song = get_object_or_404(Song, id=kwargs.get('pk'))
        serializer = SongSerializer(song, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Song unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        song = get_object_or_404(Song, id=kwargs.get('pk'))
        song.delete()

        return JsonResponse({
            'message': 'Delete Song successful!'
        }, status=status.HTTP_200_OK)


class UpdateSongView(UpdateAPIView):
    model = Song
    serializer_class = SongSerializer

    def put(self, request, *args, **kwargs):
        song = get_object_or_404(Song, id=kwargs.get('pk'))
        song.views += 1
        song.save()
        serializer = SongSerializer(song)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DetailSongView(APIView):
    model = Song
    serializer_class = SongSerializer

    def get(self, request, pk):
        song = get_object_or_404(Song, id=pk)
        serializer = SongSerializer(song)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SearchSongTitleView(APIView):
    model = Song
    serializer_class = SongSerializer

    def get(self, request, s):
        s = s.strip()
        song = Song.objects.filter(title__icontains=s)
        serializer = SongSerializer(song, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


# class SearchSongArtistView(APIView):
#     model = Song
#     serializer_class = SongSerializer
#
#     def get(self, request, s):
#         s = s.strip()
#         song = Song.objects.filter(artist__icontains=s)
#         serializer = SongSerializer(song, many=True)
#
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
