# -*- coding: UTF-8 -*-
from django.template.defaultfilters import title

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django import forms

class AccountsForm(forms.Form):
    login = forms.CharField(
        widget = forms.TextInput,
        label = u'Логин',
    )

    password = forms.CharField(
        widget = forms.PasswordInput,
        label = u'Пароль',
    )

    next = forms.CharField(
        widget = forms.HiddenInput,
    )