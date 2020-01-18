# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from django.core.mail import send_mail
from PIL import Image
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

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

@csrf_exempt
def upload(request):
    reponse_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

def process(fp,values):
    im = Image.open(fp)
    im1 = im.crop((values))
    im1.save()
    Comments_Report,Summary,list_problem,list_treatment,list_tests,dict_basic,dict_blood,dict_urine = process_img(fp)
    
    
