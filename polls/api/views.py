from rest_framework.generics import ListAPIView
from polls.models import Album
from .serializers import AlbumSerializer

class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer