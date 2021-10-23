from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('song/', views.ListCreateSongView.as_view()),
    path('song/<int:pk>', views.UpdateDeleteSongView.as_view()),
]
