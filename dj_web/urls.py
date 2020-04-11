"""dj_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url , include

from music import views


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', views.IndexView.as_view(), name='index'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^music/album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^music/album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^music/album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/', views.UserLogin.as_view(), name='login'),
    url(r'^logout/$', views.LogOut, name='logout'),
    url(r'^music/songs/$', views.SongsIndex.as_view(), name='music_songs'),
    url(r'^music/songs/add$', views.SongCreate.as_view(), name='song-add'),
    url(r'^music/songs/(?P<pk>[0-9]+)$', views.SongUpdate.as_view(), name='song-update'),
]
