from django.db import models
import os
from django.contrib.auth.models import User

class Album (models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=True)
    author = models.ForeignKey(User)
    def __unicode__ (self):
        return self.name

class Photo (models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', max_length=200)
    albums = models.ManyToManyField(Album)
    created_date = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=True)
    author = models.ForeignKey(User)
    def __unicode__ (self):
        return self.name
    def delete (self, *args, **kwargs):
        storage = self.image.storage
        path = self.image.path
        super(Photo, self).delete(*args, **kwargs)
        storage.delete(path)
