from django.forms import *
from share.models import *

class PhotoForm (ModelForm):
    class Meta:
        model = Photo

class AlbumForm (ModelForm):
    class Meta:
        model = Album

class SearchForm (Form):
    query = CharField(max_length=100)
