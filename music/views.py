from urllib.request import urlopen

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Song, Genre, SongGenre, Artist, SongArtist, User, FavoriteList
from .serializers import SongSerializer, SongSerializerPost, ArtistModelSerializer, UserRegistrationSerializer, \
    UserLoginSerializer, FavoriteListSerializer


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Register successful!'
            data['username'] = user.username

            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This username has already exist!',
                'errors_code': 409,
            }, status=status.HTTP_409_CONFLICT)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'username': serializer.validated_data['username']
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'username or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class ListSongView(ListCreateAPIView):
    permission_classes = [AllowAny]
    model = Song
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()


class ListCreateSongView(ListCreateAPIView):
    model = Song
    serializer_class = SongSerializer

    def create(self, request, *args, **kwargs):
        serializer = SongSerializerPost(data=request.data)

        if serializer.is_valid():
            artists_data = request.data['artists'].split(",")
            genres_data = request.data['genres'].split(",")
            artists = []
            for i in artists_data:
                i = i.strip()
                artists.append(i)

            genres = []
            for i in genres_data:
                i = i.strip()
                genres.append(i)

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
        serializer = SongSerializerPost(song, data=request.data)

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
    permission_classes = [AllowAny]
    model = Song
    serializer_class = SongSerializer

    def get(self, request, pk):
        song = get_object_or_404(Song, id=pk)
        serializer = SongSerializer(song)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SearchSongTitleView(APIView):
    permission_classes = [AllowAny]
    model = Song
    serializer_class = SongSerializer

    def get(self, request, s):
        s = s.strip()
        song = Song.objects.filter(title__icontains=s)
        serializer = SongSerializer(song, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SearchSongAlbumView(APIView):
    permission_classes = [AllowAny]
    model = Song
    serializer_class = SongSerializer

    def get(self, request, s):
        s = s.strip()
        song = Song.objects.filter(album=s)
        serializer = SongSerializer(song, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SongUpdateMock(APIView):

    def post(self, request):
        url = urlopen('https://mock-server-music.herokuapp.com/songs').read()
        data = json.loads(url)
        for i in data:
            if i.get('url') is None:
                song = Song.objects.create(title=i.get('title'), artwork=i.get('artwork'), url='N/A',
                                           duration=i.get('duration'), album='Default', views=0)
            else:
                song = Song.objects.create(title=i.get('title'), artwork=i.get('artwork'), url=i.get('url'),
                                           duration=i.get('duration'), album='Default', views=0)

            artists_data = i.get('artist').split(",")
            artists = []
            for j in artists_data:
                j = j.strip()
                artists.append(j)

            genres_data = i.get('genre').split(",")
            genres = []
            for j in genres_data:
                j = j.strip()
                genres.append(j)

            for j in genres:
                try:
                    genre = Genre.objects.get(title=j)
                except Genre.DoesNotExist:
                    genre = None
                if genre is None:
                    genre = Genre.objects.create(title=j)

                SongGenre.objects.create(song=song, genre=genre)

            for j in artists:
                try:
                    artist = Artist.objects.get(name=j)
                except Artist.DoesNotExist:
                    artist = None
                if artist is None:
                    artist = Artist.objects.create(name=j, information='N/A')

                SongArtist.objects.create(song=song, artist=artist)

        return Response(0, status=status.HTTP_200_OK)


class ListAlbumView(APIView):
    permission_classes = [AllowAny]
    model = Song

    def get(self, request):
        songs = Song.objects.all()
        albums = {""}
        for i in songs:
            albums.add(i.album)

        albums.remove("")

        return Response(albums, status=status.HTTP_200_OK)


class ListCreateArtistView(ListCreateAPIView):
    model = Artist
    serializer_class = ArtistModelSerializer

    def get_queryset(self):
        return Artist.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ArtistModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Create a new Artist unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteArtistView(RetrieveUpdateDestroyAPIView):
    model = Artist
    serializer_class = ArtistModelSerializer

    def put(self, request, *args, **kwargs):
        artist = get_object_or_404(Artist, id=kwargs.get('pk'))
        serializer = ArtistModelSerializer(artist, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Artist unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        artist = get_object_or_404(Artist, id=kwargs.get('pk'))
        artist.delete()

        return JsonResponse({
            'message': 'Delete Artist successful!'
        }, status=status.HTTP_200_OK)


class FavoriteListCreateAndDelete(APIView):

    def post(self, request):
        serializer = FavoriteListSerializer(data=request.data)

        if serializer.is_valid():
            song = get_object_or_404(Song, id=serializer.data['songId'])
            user = get_object_or_404(User, username=serializer.data['username'])
            FavoriteList.objects.create(song=song, user=user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Data Invalid'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        serializer = FavoriteListSerializer(data=request.data)

        if serializer.is_valid():
            song = get_object_or_404(Song, id=serializer.data['songId'])
            user = get_object_or_404(User, username=serializer.data['username'])
            favoriteList = get_object_or_404(FavoriteList, song=song, user=user)
            favoriteList.delete()

            return JsonResponse({
                'message': 'Delete Song successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Data Invalid'
        }, status=status.HTTP_400_BAD_REQUEST)


class FavoriteListView(APIView):

    def get(self, request, s):
        user = get_object_or_404(User, username=s)
        favoriteList = FavoriteList.objects.filter(user=user)
        songs = []
        for i in favoriteList:
            songs.append(i.song)

        serializer = SongSerializer(songs, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
