# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q

from tagging.models import TaggedItem, Tag

from sorl.thumbnail import delete, default, base

from photoparticipatio.libs.utils.shortcuts import json_response

from photoparticipatio.apps.gallery.forms.photo import PhotoForm
from photoparticipatio.apps.gallery.models import Album
from photoparticipatio.apps.gallery.models import Photo

import Image
import StringIO

def show(request, photo_id):
    """
    Страница фотографии
    """

    photo = get_object_or_404(Photo, pk=photo_id)
    Photo.objects.filter(pk=photo_id).update(cnt_like=F('cnt_like') + 1)

    return render(request, 'gallery/photo/show.html', locals())

@login_required
def show_by_tag(request, tag_id):
    """
    Отображение фотографий по тегу
    """

    tag = Tag.objects.get(pk=tag_id)
    photos = TaggedItem.objects.get_by_model(Photo, tag)
    photos = photos.filter(album__access=Album.ACCESS_PUBLIC)

    return render(request, 'gallery/photo/show_by_tag.html', locals())

def show_secret(request, secret, photo_id):
    """
    Отображение фотографии по прямой ссылке
    """
    photo = get_object_or_404(Photo, Q(album__secret = secret), Q(pk = photo_id))

    return render(request, 'gallery/photo/show.html', locals())

@login_required
def add(request, album_id):
    """
    Добавление фотографии
    """

    action = 'add'

    album = None
    if album_id > 0:
        album = get_object_or_404(Album, pk=album_id)

    form = PhotoForm(initial={'album': album})

    return render(request, 'gallery/photo/edit.html', locals())

@login_required
def edit(request, photo_id):
    """
    Редактирование фотографии
    """

    action = 'edit'

    photo = get_object_or_404(Photo, pk=photo_id)
    album = photo.album
    form = PhotoForm(instance = photo)

    return render(request, 'gallery/photo/edit.html', locals())

@login_required
@csrf_exempt
def transform(request, photo_id, operation):
    """
    Обработка фотографии
    """

    if request.is_ajax():
        output = {}

        try:
            photo = Photo.objects.get(pk=photo_id)

            default.kvstore.delete(base.ImageFile(photo.image))

            buffer = StringIO.StringIO()
            buffer.write(open(photo.get_abs_path(), 'rb').read())
            buffer.seek(0)

            img = Image.open(buffer)

            if operation == Photo.ROTATE_FORWARD:
                # поворот на 90 градусов по часовой стрелке

                img = img.transpose(Image.ROTATE_270)
            elif operation == Photo.ROTATE_BACKWARD:
                # поворот на 90 градусов против часовой стрелке

                img = img.transpose(Image.ROTATE_90)
            elif operation == Photo.FLIP_HORISONTAL:
                # отображение по горизонтали

                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif operation == Photo.FLIP_VERTICAL:
                # отображение по вертикали

                img = img.transpose(Image.FLIP_TOP_BOTTOM)

            img.save(photo.get_abs_path(), quality=100)

            output['status'] = u'success'
        except Photo.DoesNotExist:
            output['status'] = u'error'
            output['messages'] = u'Не удалось отредактировать фотографию. Фотография не найдена.'
        except IOError:
            output['status'] = u'error'
            output['messages'] = u'Не удалось отредактировать фотографию. Ошибка ввода-вывода.'
            output['details'] = IOError.message

        return json_response(output)
    else:
        raise Http404

@login_required
def save(request):
    """
    Сохранение фотографии
    """

    output = {}

    try:
        photo_id = int(request.POST.get('id', 0))
        if photo_id > 0:
            photo = Photo.objects.get(pk=photo_id)
        else:
            photo = Photo(
                user = request.user,
            )
        print photo_id
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save()

            output['status'] = u'success'
            output['url'] = reverse('gallery_photo_show', kwargs={
                'photo_id': photo.id,
            })
        else:
            output['status'] = u'error'
            output['messages'] = form.errors
    except Photo.DoesNotExist:
        output['status'] = u'error'
        output['messages'] = u'Не удалось обновить фотографию. Фотография не найдена.'

    return json_response(output)

@login_required
@csrf_exempt
def delete(request, photo_id):
    """
    Удаление фотографии
    """

    if request.is_ajax():
        output = {}

        try:
            photo = Photo.objects.get(pk=photo_id)
            album = photo.album
            photo.delete()

            output['status'] = 'success'
            output['url'] = reverse('gallery_album_show', kwargs={
                'album_id': album.id,
            })
        except Album.DoesNotExist:
            output['status'] = 'error'
            output['messages'] = u'Не удалось удалить фотографию. Фотография не найдена'

        return json_response(output)
    else:
        raise Http404

