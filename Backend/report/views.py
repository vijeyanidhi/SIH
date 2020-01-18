# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from django.core.mail import send_mail

# Create your views here.

@csrf_exempt
def AddTermName(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        vals = request.POST.getlist('vals')
        for x in vals:
            if not TermData.objects.filter(termName=x).exists():
                TermData.objects.create(termName=x)
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

def AddReport(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)

        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)
@csrf_exempt
def sendmail(request):

    send_mail(
        'Subject here',
        'Here is the message.',
        'vijeyanidhi@gmail.com',
        ['vijeyanidhi@gmail.com'],
        fail_silently=False,
    )
