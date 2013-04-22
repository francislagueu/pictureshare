from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import redirect_to
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pictureshare.views.home', name='home'),
    # url(r'^pictureshare/', include('pictureshare.foo.urls')),
    url(r'^$', redirect_to, {'url': '/share/'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^share/', include('share.urls')),
    url(r'^accounts/', include('registration.urls')),
)
