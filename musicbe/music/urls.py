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
    path('song/mock/', views.SongUpdateMock.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
