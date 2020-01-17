# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from login.models import *


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def login(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
        password = str(request.POST.get("password"))
        if(LoginData.objects.get(ident=ident).password == password):
            response_json['login'] = True
            response_json['loginMessage'] = 'Successful'            
        else:
            response_json['login'] = False
            response_json['LoginMessage'] = 'Incorrect username or password'
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def reset_password(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
        if LoginData.objects.filter(ident=ident).exists():
#            generate new password
            row = LoginData.objects.get(ident=ident)
#            setattr(row,'password',genpassword)
#            send mail
            response_json['reset'] = True
            response_json['resetMessage'] = 'Reset Successful'
        else:
            response_json['reset'] = False
            response_json['resetMessage'] = 'No User with the given data exist'            

        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def forgot_Ident(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        emailID = str(request.POST.get("emailID"))
        if LoginData.objects.filter(emailID=emailID).exists():
#            send mail
            response_json['forgot'] = True
            response_json['forgotMessage'] = 'EMail Successful'
        else:
            response_json['forgot'] = False
            response_json['resetMessage'] = 'No User with the given data exist'            

        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)
