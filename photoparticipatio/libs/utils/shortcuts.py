# -*- coding: UTF-8 -*-
__author__ = 'Pavlenov Semen'

from django.shortcuts import HttpResponse
import json

def json_response(output):

    return HttpResponse(json.dumps(output, sort_keys=True, indent=2),
        content_type='application/json; charset=UTF-8')