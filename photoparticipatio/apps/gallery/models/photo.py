# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField

from photoparticipatio.settings import MEDIA_URL, MEDIA_ROOT

from photoparticipatio.apps.gallery.models.album import Album

from hashlib import md5

import datetime, os

def upload_image(obj, filename):
    gallery_photos_path = MEDIA_ROOT + u'/photos'
    if os.path.exists(gallery_photos_path):
        dir_length = len(os.listdir(gallery_photos_path))
        if dir_length < 1:
            photos_path = u'photos/part_1'
        else:
            photos_path = u'photos/part_' + unicode(dir_length)
            subdir_length = len(os.listdir(MEDIA_ROOT + u'/' + photos_path))
            if subdir_length > 499:
                photos_path = u'photos/part_' + unicode(dir_length + 1)
    else:
        os.mkdir(gallery_photos_path)
        photos_path = u'photos/part_1'

    photo_name = md5(unicode(datetime.datetime.now())).hexdigest()
    photo_ext = filename.split('.').pop()

    return '{0}/{1}.{2}'.format(photos_path, photo_name, photo_ext)

class Photo(models.Model):
    ROTATE_FORWARD = u'rotateforward'
    ROTATE_BACKWARD = u'rotatebackward'
    FLIP_HORISONTAL = u'fliphorisontal'
    FLIP_VERTICAL = u'flipvertical'

    user = models.ForeignKey(
        User,
        related_name = 'photo',
        verbose_name = u'автор',
        editable = False,
    )
    album = models.ForeignKey(
        Album,
        related_name = 'photo',
        verbose_name = u'альбом',
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = u'подпись к фотографии',
    )
    date_create = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u'дата загрузки',
    )
    cnt_like = models.PositiveIntegerField(
        default = 0,
        verbose_name = u'количество лайков',
        editable = False,
    )
    image = models.ImageField(
        upload_to = upload_image,
        verbose_name = 'Изображение',
        max_length = 255,
    )
    tags = TagField(
        verbose_name = u'теги',
    )

    class Meta:
        db_table = 'gallery_photo'
        app_label = 'gallery'

    def get_abs_path(self):
        """
        Получение абсолютного пути к файлу фотографии
        """

        return MEDIA_ROOT + u'/' + unicode(self.image)

    def __unicode__(self):
        return u'<img src="{0}{1}?{3}" class="thumbnail" alt="{2}">'.format(MEDIA_URL, self.image, self.title, datetime.datetime.now())
