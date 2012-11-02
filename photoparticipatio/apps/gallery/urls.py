# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('photoparticipatio.apps.gallery.views',

    url(r'^thumb/(?P<size>.+)/$', 'thumb', name='gallery_index_thumb'),

    # Альбомы
    url(r'^album/(?P<album_id>\d+)/$', 'album.show', name='gallery_album_show'),
    url(r'^album/show/(?P<secret>.+)/$', 'album.show_secret', name='gallery_album_show_secret'),
    url(r'^album/add/$', 'album.add', name='gallery_album_add'),
    url(r'^album/(?P<album_id>\d+)/edit/$', 'album.edit', name='gallery_album_edit'),
    url(r'^album/save/$', 'album.save', name='gallery_album_save'),
    url(r'^album/(?P<album_id>\d+)/delete/$', 'album.delete', name='gallery_album_delete'),

    # Фотографии
    url(r'^photo/(?P<photo_id>\d+)/$', 'photo.show', name='gallery_photo_show'),
    url(r'^photo/show/(?P<secret>.+)/(?P<photo_id>\d+)/$', 'photo.show_secret', name='gallery_photo_show_secret'),
    url(r'^photo/tag/(?P<tag_id>\d+)/$', 'photo.show_by_tag', name='gallery_photo_show_by_tag'),
    url(r'^photo/add/$', 'photo.add', {'album_id': 0}, name='gallery_photo_add'),
    url(r'^photo/add/(?P<album_id>\d+)/$', 'photo.add', name='gallery_photo_add_to_album'),
    url(r'^photo/(?P<photo_id>\d+)/edit/$', 'photo.edit', name='gallery_photo_edit'),
    url(r'^photo/(?P<photo_id>\d+)/transform/(?P<operation>[a-z]+)/$', 'photo.transform', name='gallery_photo_transform'),
    url(r'^photo/save/$', 'photo.save', name='gallery_photo_save'),
    url(r'^photo/(?P<photo_id>\d+)/delete/$', 'photo.delete', name='gallery_photo_delete'),
)
