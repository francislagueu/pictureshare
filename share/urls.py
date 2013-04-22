from django.conf.urls.defaults import patterns, include, url

from share import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^albums/(\d+)/$', views.album, name='album'),
    url(r'^photos/(\d+)/$', views.photo, name='photo'),
    url(r'^albums/delete/(\d+)/$', views.delete_album, name='delete_album'),
    url(r'^photos/delete/(\d+)/$', views.delete_photo, name='delete_photo'),
    url(r'^albums/privacy/(\d+)/(\w+)/$', views.change_album_privacy, name='change_album_privacy'),
    url(r'^photos/privacy/(\d+)/(\w+)/$', views.change_photo_privacy, name='change_photo_privacy'),
    url(r'^img/(\d+)/$', views.img, name='img'),
)
