from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'music'
urlpatterns = [
    path('song/', views.ListCreateSongView.as_view()),
    path('song/<int:pk>', views.UpdateDeleteSongView.as_view()),
    path('song/views/<int:pk>', views.UpdateSongView.as_view()),
    path('song/detail/<int:pk>', views.DetailSongView.as_view()),
    path('song/search/title/<str:s>', views.SearchSongTitleView.as_view()),
    path('song/search/album/<str:s>', views.SearchSongAlbumView.as_view()),
    path('song/album/', views.ListAlbumView.as_view()),
    path('song/mock/', views.SongUpdateMock.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('artist/', views.ListCreateArtistView.as_view()),
    path('artist/<int:pk>', views.UpdateDeleteArtistView.as_view()),
    path('register', views.registration_view, name='register'),
    path('login', views.UserLoginView.as_view(), name='login'),
]
