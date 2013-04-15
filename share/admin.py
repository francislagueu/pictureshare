from django.contrib import admin
from share.models import *

class PhotoInline (admin.StackedInline):
    model = Photo.albums.through
    extra = 1

class AlbumAdmin (admin.ModelAdmin):
    inlines = [PhotoInline]

class PhotoAdmin (admin.ModelAdmin):
    inlines = [PhotoInline]
    exclude = ('albums',)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
