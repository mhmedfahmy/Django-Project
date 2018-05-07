from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    
    #/music 
    path('', views.indexView.as_view() , name='index'),
    #/music/22/
    path('<album_id>/', views.indexDetail.as_view(), name='detail'),
    #user
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    #/music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    #/music/album/add
    path('album/<album_id>/delete', views.AlbumDelete.as_view(), name='album-delete'),
    #create_song
    path('<album_id>/createsong/', views.CreateSong, name='createsong'),

]