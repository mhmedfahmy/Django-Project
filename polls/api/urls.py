from django.urls import path
from polls.api.views import (
    AlbumListAPIView
)

urlpatterns = [
    
    #/music 
    path('', AlbumListAPIView.as_view() , name='index'),
    
]