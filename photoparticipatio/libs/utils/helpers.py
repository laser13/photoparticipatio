# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

def get_form_errors(form):

    return dict((k, map(unicode, v)) for (k,v) in form.errors.iteritems())

def var_dump(dict):

    print "\n", ' = {'
    for key, value in dict.iteritems():
        print '"{0}" => "{1}"'.format(key, value), "\n"
    print '}', "\n"