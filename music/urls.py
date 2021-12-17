from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'music'
urlpatterns = [
    path('song/all', views.ListSongView.as_view()),
    path('song/', views.ListCreateSongView.as_view()),
    path('song/<int:pk>', views.UpdateDeleteSongView.as_view()),
    path('song/views/<int:pk>', views.UpdateSongView.as_view()),
    path('song/detail/<int:pk>', views.DetailSongView.as_view()),
    path('song/search/title/<str:s>', views.SearchSongTitleView.as_view()),
    path('song/mock/', views.SongUpdateMock.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('artist/', views.ListCreateArtistView.as_view()),
    path('artist/<int:pk>', views.UpdateDeleteArtistView.as_view()),
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('favorite-list/', views.FavoriteListCreateAndDelete.as_view()),
    path('favorite-list/<str:s>', views.FavoriteListView.as_view()),
    path('genre/all', views.ListGenreView.as_view()),
    path('genre-song/<str:s>', views.SearchSongGenreView.as_view()),
    path('genre/', views.ListCreateGenreView.as_view()),
    path('genre/<int:pk>', views.UpdateDeleteGenreView.as_view()),
    path('playlist/all', views.ListPlaylistView.as_view()),
    path('playlist-song/<int:pk>', views.SearchSongPlaylistView.as_view()),
    path('playlist/', views.ListCreatePlaylistView.as_view()),
    path('playlist/<int:pk>', views.UpdateDeletePlaylistView.as_view()),
    path('playlist-song/', views.PlayListSongCreateAndDelete.as_view()),
    path('playlist/detail/<int:pk>', views.PlaylistView.as_view()),
    path('playlist-user/<str:s>', views.PlaylistUserView.as_view()),
]
