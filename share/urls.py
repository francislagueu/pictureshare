from django.conf.urls.defaults import patterns, include, url

from share import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)