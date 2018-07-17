# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import loader
import datetime
def index(request):
    return render(request,'index.html')
    #template=loader.get_template('index.html')
    #name= {
     #   'student':'srinivas'
    #}
    #return HttpResponse(template.render(name))
    #now=datetime.datetime.now()
    #html="<html><body><h3>Now time is %s.</h3></body></html>"%now
    #return HttpResponse(html)
# Create your views here.
@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h2>this is http GET request.</h2>')