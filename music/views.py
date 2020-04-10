from django.shortcuts import render
from django.http import HttpResponse
from .models import Album , Song

# Create your views here.

def index(request):
    album_list = Album.objects.all()
    return render(request , 'music/index.html' , { 'all_album' : album_list })

def detail(request , album_id):
    return HttpResponse("<h1> welcome to Detail Page  </h1>")