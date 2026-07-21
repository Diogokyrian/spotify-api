from rest_framework import viewsets
from .models import Singer, Album
from .serializers import SingerSerializer, AlbumSerializer
from .filtering import singer_filter_fields, album_filter_fields

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    filterset_fields = singer_filter_fields

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filterset_fields = album_filter_fields