# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django import forms

from photoparticipatio.apps.gallery.models.album import Album

class AlbumForm(forms.ModelForm):
    id = forms.IntegerField(
        widget = forms.HiddenInput,
    )

    class Meta:
        model = Album

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args,**kwargs)
        self.fields['title'].error_messages = {
            'required': u'Укажите название альбома',
        }
