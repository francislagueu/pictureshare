from django.http import HttpResponse
from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render
from share.models import *
from settings import MEDIA_URL
from itertools import chain
from operator import attrgetter

def index (request):
    public_albums = Album.objects.filter(private=False)
    public_photos = Photo.objects.filter(private=False).order_by('-created_date')[:5];
    private_albums = []
    private_photos = []

    if request.user.is_authenticated():
      private_albums = Album.objects.filter(author=request.user);
      private_photos = Photo.objects.filter(author=request.user);

    latest_albums = sorted(chain(public_albums, private_albums), key=attrgetter('modified_date'))[:5];
    latest_photos = sorted(chain(public_photos, private_photos), key=attrgetter('created_date'))[:5];
    
    context = {
        'latest_albums': latest_albums,
        'latest_photos': latest_photos,
    }

    return render(request, 'share/index.html', context)

def photo (request, pk):
    img = Photo.objects.get(pk=pk)
    if img.private and not request.user==img.author:
        return render(request, "share/access_denied.html")

    context = {
        'image': img,
        'user': request.user,
        'backurl': request.META["HTTP_REFERER"],
        'media_url' : MEDIA_URL,
    }
    return render(request, "share/photo.html", context)

def album(request, pk):
    album = Album.objects.get(pk=pk)

    if album.private and not request.user==album.author:
        return render(request, "share/access_denied.html")
    
    images = Photo.objects.filter(albums__id=pk)
    paginator = Paginator(images, 30)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)
    
    context = {
        'album' : album,
        'images' : images,
        'user' : request.user,
        'media_url' : MEDIA_URL,
    }
    return render(request, "share/album.html", context)
