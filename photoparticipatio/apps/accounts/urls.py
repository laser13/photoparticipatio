# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django.conf.urls import patterns, include, url

from django.views.generic.base import TemplateView

from registration.views import activate
from registration.views import register
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = patterns('photoparticipatio.apps.accounts.views',
    url(r'^$', 'index', name='accounts_index'),
    url(r'^login/$', 'login', name='accounts_login'),
    url(r'^logout/$', 'logout', name='accounts_logout'),
)

# Регистрация
urlpatterns += patterns('',
    url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', activate, {'backend':'registration.backends.default.DefaultBackend'}, name='registration_activate'),
    url(r'^register/$', register, {'backend':'registration.backends.default.DefaultBackend', 'form_class': RegistrationFormUniqueEmail}, name='registration_register'),
    url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'), (r'', include('registration.auth_urls')),
)