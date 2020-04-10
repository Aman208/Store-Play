from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Album , Song

# Create your views here.

def index(request):
    album_list = Album.objects.all()
    return render(request , 'music/index.html' , { 'all_album' : album_list })

def detail(request , album_id):
    album = get_object_or_404(Album , pk=album_id)
    return render(request , 'music/detail.html', {'album': album} )
    