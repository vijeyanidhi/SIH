# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from django.core.mail import send_mail

import os
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
        ident = str(request.POST.get("ident"))
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

def process(ident,fp,values):
    im = Image.open(fp)
    im1 = im.crop((values))
    im1.save()
    dict_basic, dict_blood, dict_urine, dict_liver, dict_stool, Comments_Report, Summary, list_problem, list_treatment, list_tests = information_extract(fp)
    reportID = str(datetime.now().strftime("%d/%m/%Y-%H:%M"))
    if(len(Comments_Report)==0):
        Comments_Report="None"
    if(len(Summary)==0):
        Summary="None"
    ReportString.objects.create(ident=LoginData.objects.get(ident=ident),reportID=reportID,comments=Comments_Report,summary=Summary)

    ReportStringInstance = ReportString.objects.get(reportID=reportID)
    
    for x,y in dict_blood:
        ReportValues.objects.create(reportID=ReportStringInstance,report_type="blood report",reportKey=x,reportValue=y)
    for x,y in dict_urine:
        ReportValues.objects.create(reportID=ReportStringInstance,report_type="urine report",reportKey=x,reportValue=y)
    for x,y,z in dict_liver:
        ReportValues.objects.create(reportID=ReportStringInstance,report_type="liver report",reportKey=x,reportValue=y)
    for x,y in dict_urine:
        ReportValues.objects.create(reportID=ReportStringInstance,report_type="stool report",reportKey=x,reportValue=y)

    for x,y in dict_basic:
        ReportBasic.objects.create(reportID=ReportStringInstance,reportKey=x,reportValue=y)

    for x in list_problem:
        ReportList.objects.create(reportID=ReportStringInstance,reportKey="problem",reportValue=x)
    for x in list_treatment:
        ReportList.objects.create(reportID=ReportStringInstance,reportKey="treatment",reportValue=x)
    for x in list_test:
        ReportList.objects.create(reportID=ReportStringInstance,reportKey="test",reportValue=x)

@csrf_exempt
def sendReportID(request):
    response_json = {}
    ret_list = []
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        for x in ReportString.objects.all().values("reportID").distinct():
            ret_list.append(x)
        response_json['data_list'] = ret_list
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def sendReportStrings(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportInstance = ReportString.objects.filter(reportID=reportID)
        response_json['comment'] = reportInstance.comment
        response_json['summary'] = reportInstance.summary
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def sendReportvalues(request):
    response_json = {}
    dl1 = []
    dl2 = []
    dl3 = []
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportInstance = ReportString.objects.filter(reportID=reportID)
        for x in ReportValues.objects.filter(reportID=reportInstance):
            dl1.append(x.type)
            dl2.append(x.key)
            dl3.append(x.value)
        response_json['type'] = dl1
        response_json['key'] = dl2
        response_json['value'] = dl3
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def sendReportBasicvalues(request):
    response_json = {}
    dl1 = []
    dl2 = []
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportInstance = ReportString.objects.filter(reportID=reportID)
        for x in ReportBasic.objects.filter(reportID=reportInstance):
            dl1.append(x.key)
            dl2.append(x.value)
        response_json['key'] = dl1
        response_json['value'] = dl2
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def sendReportListvalues(request):
    response_json = {}
    dl1 = []
    dl2 = []
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportInstance = ReportString.objects.filter(reportID=reportID)
        for x in ReportList.objects.filter(reportID=reportInstance):
            dl1.append(x.key)
            dl2.append(x.value)
        response_json['key'] = dl1
        response_json['value'] = dl2
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)


@csrf_exempt
def sendTotalReport(request):
    response_json = {}

    dl1 = []
    dl2 = []
    dl3 = []
    dl4 = []
    dl5 = []
    dl6 = []
    dl7 = []

    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportInstance = ReportString.objects.filter(reportID=reportID)

        for x in ReportList.objects.filter(reportID=reportInstance):
            dl1.append(x.reportKey)
            dl2.append(x.reportValue)

        for x in ReportBasic.objects.filter(reportID=reportInstance):
            dl3.append(x.reportKey)
            dl4.append(x.reportValue)

        for x in ReportValues.objects.filter(reportID=reportInstance):
            dl5.append(x.reporttype)
            dl6.append(x.reportKey)
            dl7.append(x.reportValue)
        print(reportID)
        response_json['comment'] = ReportString.objects.get(reportID=reportID).comments
        response_json['summary'] = ReportString.objects.get(reportID=reportID).summary

        response_json['listkey'] = dl1
        response_json['listvalue'] = dl2

        response_json['basickey'] = dl3
        response_json['basicvalue'] = dl4

        response_json['reptype'] = dl5
        response_json['repkey'] = dl6
        response_json['repvalue'] = dl7

        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"
    print (str(response_json))
    return JsonResponse(response_json)
