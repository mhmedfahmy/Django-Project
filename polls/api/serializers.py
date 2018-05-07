from rest_framework.serializers import ModelSerializer
from polls.models import Album

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'artist',
            'album_title',
            'genre',
        ]