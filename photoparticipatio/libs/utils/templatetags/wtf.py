# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from django import template
from django.template.defaultfilters import linebreaksbr
from django.utils.html import escape
import inspect
try:
    from django.utils.safestring import mark_safe
except ImportError: # v0.96 and 0.97-pre-autoescaping compat
    def mark_safe(x): return x
from pprint import pformat

def rawdump(x):
    if hasattr(x, '__dict__'):
        d = {
            '__str__':str(x),
            '__unicode__':unicode(x),
            '__repr__':repr(x),
            }
        d.update(x.__dict__)
        x = d
    output = pformat(x)+'\n'
    return output

register = template.Library()
@register.inclusion_tag("utils/wtf/dump.html", takes_context=True)
def wtf(context, object,):
    try:
        context['dir'] = dir(object)
        context['object'] = object
        context['class'] = u'{0}'.format(object.__class__)
#        context['dump'] = mark_safe(linebreaksbr(escape(rawdump(object))))

#        print inspect.getmembers(object, predicate=inspect.ismethod)

        import types

        methods = [a for a in dir(object)
            if hasattr(object, a) and isinstance(getattr(object, a), types.MethodType)]

        attribs = [[a, getattr(object, a)] for a in dir(object)
                   if hasattr(object, a) and
                      (
                          isinstance(getattr(object, a), types.BooleanType) or
                          isinstance(getattr(object, a), types.UnicodeType) or
                          isinstance(getattr(object, a), types.IntType) or
                          isinstance(getattr(object, a), types.FloatType) or
                          type(getattr(object, a)) == 'datetime.datetime' or
                          isinstance(getattr(object, a), types.StringType)
                        )
                ]

        print attribs

        context['methods'] = methods
        context['attribs'] = attribs
#        print dir(classmethod(object))
#        print hasattr(object, 'pk')
#        print getattr(object, 'pk')
#        print callable(getattr(object, 'pk'))
#        for item in context['dir']:
#            try:
#                print type(getattr(object, item))
#            except Exception, e:
#                print e
#            attr = getattr(object, item)
#            pri

    except Exception,e:
        print e
    return context