from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Song
from .serializers import SongSerializer


class ListCreateSongView(ListCreateAPIView):
    model = Song
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

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
        song = Song.objects.filter(title__icontains=s)
        serializer = SongSerializer(song, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SearchSongArtistView(APIView):
    model = Song
    serializer_class = SongSerializer

    def get(self, request, s):
        song = Song.objects.filter(artist__icontains=s)
        serializer = SongSerializer(song, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
