from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from share.models import *

def index (request):
    latest_albums = Album.objects.order_by('-modified_date')[:5];
    latest_photos = Photo.objects.order_by('-created_date')[:5];
    context = {
        'latest_albums': latest_albums,
        'latest_photos': latest_photos,
    }
    return render(request, 'share/index.html', context)