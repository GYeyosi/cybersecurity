# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def practiceindex(request):
    if request.user.is_authenticated():
        return HttpResponse("Hello, Practice Index page")
    else:
        return HttpResponseRedirect('/login')

    