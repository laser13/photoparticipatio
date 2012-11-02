# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):

    ACCESS_PRIVATE = 0
    ACCESS_PUBLIC = 1

    CHOICES_ACCESS = (
        (ACCESS_PRIVATE, u'закрытый'),
        (ACCESS_PUBLIC, u'открытый'),
    )

    KIND_DEFAULT = 0
    KIND_CUSTOM = 1

    CHOICES_KIND = (
        (KIND_DEFAULT, 'default'),
        (KIND_CUSTOM, 'custom'),
    )

    user = models.ForeignKey(
        User,
        related_name = 'album',
        editable = False,
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'название',
    )
    kind = models.PositiveSmallIntegerField(
        choices = CHOICES_KIND,
        editable = False,
        default = 1,
    )
    access = models.PositiveSmallIntegerField(
        choices = CHOICES_ACCESS,
        default = 0,
        verbose_name = 'доступ',
    )
    secret = models.CharField(
        max_length = 32,
        editable = False,
        default = '',
    )

    def __unicode__(self):
        return self.title

    def is_owner(self, user):
        can_edit = False
        if user.is_authenticated() and (user == self.user or user.is_superuser):
            can_edit = True

        return can_edit

    class Meta:
        db_table = 'gallery_album'
        app_label = 'gallery'
