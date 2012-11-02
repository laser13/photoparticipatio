# -*- coding: UTF-8 -*-
__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.shortcuts import render

from photoparticipatio.apps.gallery.models.photo import Photo
from photoparticipatio.apps.gallery.models.album import Album

def index(request):

    photos = Photo.objects.filter(album__access=Album.ACCESS_PUBLIC).select_related()

    return render(request, 'gallery/index.html', locals())

def thumb(request, size):

    photos = Photo.objects.filter(album__access=Album.ACCESS_PUBLIC).select_related()

    if size == '170x170':
        template = 'gallery/snippets/thumb170x170.html'
    if size == '570x350':
        template = 'gallery/snippets/thumb570x350.html'

    return render(request, template, locals())

