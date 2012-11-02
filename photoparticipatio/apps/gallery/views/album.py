# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from hashlib import md5
from time import time

from photoparticipatio.libs.utils.shortcuts import json_response

from photoparticipatio.apps.gallery.models.album import Album
from photoparticipatio.apps.gallery.forms.album import AlbumForm
from photoparticipatio.apps.gallery.models.photo import Photo

def show(request, album_id):
    """
        Отображение страницы альбома
        Неавторизованный пользователь может просматривать публичные альбомы
        Авторизованный пользователь может просматривать публичные альбомы других пользователей и все свои
    """

    if not request.user.is_authenticated():
        album = get_object_or_404(Album, pk=album_id, access=Album.ACCESS_PUBLIC)
    else:
        album = get_object_or_404(Album, pk=album_id)

        if album.access == Album.ACCESS_PRIVATE and not album.is_owner(request.user):
            raise Http404

    photos = Photo.objects.filter(album=album)

    return render(request, 'gallery/album/show.html', locals())

def show_secret(request, secret):
    """
    Отображение страницы альбома по прямой ссылке
    """

    album = get_object_or_404(Album.objects.select_related(), secret=secret)
    photos = album.photo.all()

    return render(request, 'gallery/album/show.html', locals())

@login_required
def add(request):
    """
    Отображение страницы добавления альбома
    """

    action = 'add'

    form = AlbumForm(initial={'id': 0})

    return render(request, 'gallery/album/edit.html', locals())

@login_required
def edit(request, album_id):
    """
    Отображение страницы редактирования альбома
    """

    action = 'edit'

    album = get_object_or_404(Album, pk=album_id)
    form = AlbumForm(instance=album)

    return render(request, 'gallery/album/edit.html', locals())

@login_required
def save(request):
    """
    Сохранение альбома
    """

    if request.is_ajax():
        output = {}

        try:
            album_id = int(request.POST.get('id', 0))
            if album_id > 0:
                album = Album.objects.get(pk=album_id)
            else:
                album = Album(
                    user = request.user,
                    secret = md5(unicode(time())).hexdigest(),
                )

            form = AlbumForm(request.POST, instance=album)
            if form.is_valid():
                album = form.save()

                output['status'] = u'success'
                output['album_id'] = album.pk
                output['url'] = reverse('gallery_album_show', kwargs={
                    'album_id': album.id,
                })
            else:
                output['status'] = u'error'
                output['messages'] = form.errors
        except Album.DoesNotExist:
            output['status'] = u'error'
            output['messages'] = u'Не удалось обновить альбом. Альбом не найден.'

        return json_response(output)
    else:
        raise Http404

@login_required
@csrf_exempt
def delete(request, album_id):
    """
    Удаление альбома
    """

    if request.is_ajax():
        output = {}

        try:
            album = Album.objects.get(pk=album_id)
            album.delete()

            output['status'] = 'success'
            output['url'] = reverse('home')
        except Album.DoesNotExist:
            output['status'] = 'error'
            output['messages'] = u'Не удалось удалить альбом. Альбом не найден'

        return json_response(output)
    else:
        raise Http404
