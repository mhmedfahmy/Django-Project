from django.views import generic
from django import forms
from django.views.generic.edit import CreateView, DeleteView
from .models import Album
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from .forms import UserForm, SongForm


class indexView(generic.ListView):
    template_name = 'music/index.html'
    def get_queryset(self):
        return Album.objects.all()

class indexDetail(generic.DetailView):
    model=Album
    pk_url_kwarg = 'album_id'
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model=Album
    fields=['artist', 'album_title', 'genre', 'album_logo']
    template_name='music/album_form.html'
    success_url = reverse_lazy('polls:index')

class AlbumDelete(DeleteView):
    model=Album
    pk_url_kwarg = 'album_id'
    success_url=reverse_lazy('polls:index')

def logout_user(request):
    logout(request)
    return redirect('/polls')


def login_user(request):
    form = UserForm(request.POST or None)
    title = "Login"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return redirect('/polls', {'albums': albums})
            else:
                return render(request, 'music/SignUp.html', {"form": form, "title":title})
        else:
            return render(request, 'music/SignUp.html', {"form": form, "title":title})
    return render(request,'music/SignUp.html',{"form": form, "title":title})

def register(request):
    form = UserForm(request.POST or None)
    title = "Register"
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'music/index.html')
    context = {
        "form": form,
        "title":title
    }
    return render(request, 'music/SignUp.html', context)

def CreateSong(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    AUDIO_FILE_TYPES = ['mp3']
    if form.is_valid():
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        if file_type not in AUDIO_FILE_TYPES:
            raise forms.ValidationError("Audio file must be  MP3") 
        else:
            song.save()
            return render(request, 'music/detail.html', {'album': album})
        
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/song_form.html', context)