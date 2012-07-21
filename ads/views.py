# -*- coding: utf-8 -*-
# Create your views here.
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect, HttpRequest
from django.shortcuts import render_to_response
from ads.models import *

@login_required
def home(request):
    assert isinstance(request,HttpRequest)
    if request.method=="GET":
        context={}
        context["user"]=request.user
        ads=AdUser.objects.filter(user=request.user).filter(end_time__gt=datetime.datetime.now()).all()
        context["ads"]=ads
        userad=Ad.objects.filter(aduser__in=ads).all()
        context["userad"]=userad


        return render_to_response("index.html",context)
    elif request.method=="POST":
        #TODO: 上传
        return render_to_response("index.html")

