# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.shortcuts import render, redirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from photoparticipatio.libs.utils.shortcuts import json_response

from photoparticipatio.apps.accounts.forms import AccountsForm

def index(request):
    """
    Отображение страницы аутентификации
    """

    form = AccountsForm(initial={'next': request.GET.get('next', '/')})

    return render(request, 'accounts/index.html', locals())

def login(request):
    """
    Вход в систему
    После входа пользователя в систему, он перенаправляется на последнюю посещенную страницу или на главную
    """

    if request.is_ajax():
        output = {}

        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)

            output['status'] = u'success'
            output['url'] = request.POST.get('next', reverse('home'))
        else:
            output['status'] = u'error'
            output['messages'] = u'Указан неверный логин или пароль'

        return json_response(output)
    else:
        raise Http404

@login_required
def logout(request):
    """
    Выход из системы
    После выхода из системы, пользователь перенаправляется на главную страницу
    """

    auth.logout(request)

    return redirect('home')