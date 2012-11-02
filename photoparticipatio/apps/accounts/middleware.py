# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from photoparticipatio.apps.accounts.forms import AccountsForm

class AuthMiddleware:

    def process_request(self, request):
        form = AccountsForm(initial={'next': request.GET.get('next', '/')})
        setattr(request, 'auth_form', form)