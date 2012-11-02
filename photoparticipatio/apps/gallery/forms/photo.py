# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django import forms

from photoparticipatio.apps.gallery.models.photo import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo


    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args,**kwargs)
        self.fields['title'].error_messages = {
            'required': u'Укажите подпись к фотографии',
        }
        self.fields['image'].error_messages = {
            'required': u'Выберите фотографию',
        }
