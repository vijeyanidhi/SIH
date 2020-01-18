# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from login.models import *

import random
from datetime import datetime, timedelta 
from dateutil.relativedelta import relativedelta

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Mail import sendMail

# Create your views here.
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def ranint(y):
       return ''.join(str(random.randint(0,9)) for x in range(y))


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
            genpassword(10)
            row = LoginData.objects.get(ident=ident)
            setattr(row,'password',genpassword)
            row.save()
            message = 'Password for your account has been successfully reset to ' + genpassword + '. Please be careful in the future.'
            sendMail('Password Reset',message,ResetData.objects.get(ident=row).emailID)
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
            identInstance = ResetData.objects.get(emailID=emailID).ident
            message = 'Username for your account is ' + identInstance.ident + '. Please be careful in the future.'
            sendMail('Username',message,emailID)
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

@csrf_exempt
def verify1(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        emailID = str(request.POST.get("emailID"))
        OTP = 124# 
        message = 'OTP for your account verification is ' + str(OTP)
        sendMail('OTP For email Verification',message,emailID)
        stop = datetime.now() + timedelta(minutes = 15)
        stop = stop.strftime("%d/%m/%Y %H:%M:%S")
        OTPData.objects.create(emailID=emailID,otp=OTP,stop=stop)
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)


def diff(t_a, t_b,val):
    t_diff = relativedelta(t_b, t_a)
    if(t_diff.hours>0 or t_diff.minutes > val):
        return False
    else:
        return True

@csrf_exempt
def verify2(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        emailID = str(request.POST.get("emailID"))
        OTP = int(request.POST.get("OTP"))
            
        OTPDataInstance = OTPData.objects.get(emailID=emailID)
        stop = datetime.strptime(OTPDataInstance.stop, '%d/%m/%Y %H:%M:%S')
        if(OTPDataInstance.otp == OTP and diff(datetime.now,stop,15)):
            setattr(OTPDataInstance,'flag',True)
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

def renderSignIn(request):
    return render(request, 'signup.html')
