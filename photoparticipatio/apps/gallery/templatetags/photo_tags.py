# -*- coding: UTF-8 -*-

__author__ = 'G@mOBEP'
__company__ = 'RealWeb'

from django import template

register = template.Library()
@register.inclusion_tag('gallery/photo/templatetags/photo_tags.html')
def photo_tags(photo):
    return {'photo': photo}
