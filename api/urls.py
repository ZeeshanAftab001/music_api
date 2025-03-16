from django.urls import path
from .views import ArtistListCreateView, AlbumListCreateView, SongListCreateView

urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name='artist-list'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    path('songs/', SongListCreateView.as_view(), name='song-list'),
]
