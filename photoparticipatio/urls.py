# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photoparticipatio.views.home', name='home'),
    # url(r'^photoparticipatio/', include('photoparticipatio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'photoparticipatio.apps.gallery.views.__init__.index', name='home'),
    url(r'^gallery/', include('photoparticipatio.apps.gallery.urls'), name='gallery'),
    url(r'^accounts/', include('photoparticipatio.apps.accounts.urls'), name='accounts'),
)



# Статика
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()