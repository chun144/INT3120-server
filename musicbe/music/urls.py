from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('song/', views.ListCreateSongView.as_view()),
    path('song/<int:pk>', views.UpdateDeleteSongView.as_view()),
    path('song/views/<int:pk>', views.UpdateSongView.as_view()),
    path('song/detail/<int:pk>', views.DetailSongView.as_view()),
    path('song/search/title/<str:s>', views.SearchSongTitleView.as_view()),
    path('song/search/artist/<str:s>', views.SearchSongArtistView.as_view()),
]
