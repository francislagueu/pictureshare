from django.forms import *
from share.models import *

class PhotoForm (ModelForm):
    def __init__ (self, *args, **kwargs):
        user = kwargs.pop('user')
        if not user.is_authenticated():
            user = None
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['albums'] = ModelMultipleChoiceField(queryset=Album.objects.all().filter(author=user)) 
    class Meta:
        model = Photo

class AlbumForm (ModelForm):
    class Meta:
        model = Album

class SearchForm (Form):
    query = CharField(max_length=100)
