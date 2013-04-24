from django.http import HttpResponse
from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import redirect
from django.shortcuts import render
from share.models import *
from itertools import chain
from operator import attrgetter
from settings import MEDIA_ROOT
import os, mimetypes
from django.core.servers.basehttp import FileWrapper
from share.forms import * 

def index (request):
    public_albums = Album.objects.filter(private=False)
    public_photos = Photo.objects.filter(private=False)
    private_albums = []
    private_photos = []

    if request.user.is_authenticated():
      private_albums = Album.objects.filter(private=True).filter(author=request.user);
      private_photos = Photo.objects.filter(private=True).filter(author=request.user);

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
    }
    return render(request, "share/photo.html", context)

def img (request, pk):
    img = Photo.objects.get(pk=pk)
    if img.private and not request.user==img.author:
        return render(request, "share/access_denied.html")
    ifile = open(img.image.path, 'rb')
    fn, fe = os.path.splitext(img.image.path)
    wrapper = FileWrapper(ifile)
    response = HttpResponse(wrapper, mimetype=mimetypes.guess_type(img.image.path))
    response['Content-Disposition'] = 'filename="%s"' % ifile.name
    response['Content-Length'] = os.path.getsize(img.image.path)
    return response

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
    }
    return render(request, "share/album.html", context)

def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.user==album.author:
        album.delete()
        return redirect('index')
    else:
        return render(request, "share/access_denied.html")

def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.user==photo.author:
        photo.delete()
        return redirect('index')
    else:
        return render(request, "share/access_denied.html")
   

def change_album_privacy(request, pk, private):
    album = Album.objects.get(pk=pk)
    if request.user==album.author:
        album.private = private.startswith('T')
        album.save()
        return redirect('album', pk)
    #return HttpResponse(str(album.private) + " " +str(private) + " " + str(private != 0));
    else:
        return render(request, "share/access_denied.html")

def change_photo_privacy(request, pk, private):
    photo = Photo.objects.get(pk=pk)
    if request.user==photo.author:
        photo.private = private.startswith('T')
        photo.save()
        return redirect('photo', pk)
    else:
        return render(request, "share/access_denied.html")

def upload_photo(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES,
                             instance = Photo(author=request.user))
            if form.is_valid():
                photo = form.save()
                return redirect('index')
        else:
            form = PhotoForm()
        return render(request, 'share/upload_photo.html', {'form': form})
    else:
        return render(request, 'share/access_denied.html')

def add_album(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AlbumForm(request.POST, request.FILES,
                             instance = Album(author=request.user))
            if form.is_valid():
                album = form.save()
                return redirect('album', album.pk)
        else:
            form = AlbumForm()
        return render(request, 'share/add_album.html', {'form': form})
    else:
        return render(request, 'share/access_denied.html')
