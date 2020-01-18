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

@csrf_exempt
def AddReport(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
# get data form OCR 
        IdentInstance = LoginData.objects.get(ident=ident)
#        doctorName
#        Report.objects.create(reportID = reportID,customerIdent=IdentInstance,doctorName=doctorName)
#        ReportIDInstance=Report.objects.get(reportID=reportID)
#        for x in data:    
#            ReportContent.objects.create(ReportID = ReportIDInstance,termName=TermData.objects.get(termName=termName),value=value,units=units,refValue=refValue)
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def reportList(request):
    reponse_json = {}
    retlist = []
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
        for x in Report.objects.filter(customerIdent = LoginData.objects.get(ident=ident)):
            retlist.append(x.reportID)
        response_json['data'] = retlist
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def reportContent(request):
    reponse_json = {}
    retlist = []
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        for x in ReportContent.objects.filter(ReportID = Report.objects.get(reportID=reportID)):
            contentList = {'termName':x.termName,'value':x.value,'untis':x.units,'refValue':refValue}
            retlist.append(contentList)
        response_json['data'] = retlist
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)


