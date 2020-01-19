# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from Mail import sendMail
from datetime import datetime, timedelta 

import os
from PIL import Image

from Information import information_extract
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
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
        values = str(request.POST.get("values"))
        fn = ident+str(datetime.now().strftime("%d-%m-%Y-%H:%M"))+'.jpg'
        handle_uploaded_file(request.FILES['file'], fn)
        path = "/home/amit/SIH/Backend/upload/"+fn
        print(path)
        process(ident,path,values)
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

def process(ident,fp,values):
    dict_basic, dict_blood, dict_urine, dict_liver, dict_stool, Comments_Report, Summary, list_problem, list_treatment, list_test = information_extract(fp)
    reportID = str(datetime.now().strftime("%d/%m/%Y-%H:%M"))
    if(len(Comments_Report)==0):
        Comments_Report="None"
    if(len(Summary)==0):
        Summary="None"
    
    ReportString.objects.create(reportID=reportID,comments=Comments_Report,summary=Summary)

    ReportStringInstance = ReportString.objects.get(reportID=reportID)
    if dict_blood is not None:
        for x,y in dict_blood.items():
            ReportValues.objects.create(reportID=ReportStringInstance,reporttype="blood report",reportKey=x,reportValue=y)

    if dict_urine is not None:
        for x,y in dict_urine.items():
            ReportValues.objects.create(reportID=ReportStringInstance,reporttype="urine report",reportKey=x,reportValue=y)
    
    if dict_liver is not None:
        for x,y in dict_liver.items():
            ReportValues.objects.create(reportID=ReportStringInstance,reporttype="liver report",reportKey=x,reportValue=y)
    
    if dict_stool is not None:
        for x,y in dict_stool.items():
            ReportValues.objects.create(reportID=ReportStringInstance,reporttype="stool report",reportKey=x,reportValue=y)

    if dict_basic is not None:
        for x,y in dict_basic.items():
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
#        emailID = str(request.POST.get("email"))
#        ResetDataInstance = ResetData.objects.get(emailID=emailID)
#        LoginDataInstance = ResetDataInstance.ident
#        for x in ReportString.objects.filter(ident=LoginDataInstance).distinct():
#            ret_list.append(x)
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

    dl1 = {}

    problem=[]
    treatment=[]
    test=[]

    dl2 = {}

    dl3 = {}

    blood={}
    urine={}
    liver={}
    stool={}

    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportInstance = ReportString.objects.filter(reportID=reportID)

        for x in ReportList.objects.filter(reportID=reportInstance):
            if(x.reportKey=="problem"):
                problem.append(x.reportValue)
            elif(x.reportKey=="treatment"):
                treatment.append(x.reportValue)
            elif(x.reportKey=="test"):
                test.append(x.reportValue)

        dl1['problem'] = problem
        dl1['treatment'] = treatment
        dl1['test'] = test

        for x in ReportBasic.objects.filter(reportID=reportInstance):
            dl2[x.reportKey]=x.reportValue

        for x in ReportValues.objects.filter(reportID=reportInstance):
            if(x.reporttype == "blood report"):
                blood[x.reportKey] = x.reportValue
            elif(x.reporttype == "urine report"):
                urine[x.reportKey] = x.reportValue  
            elif(x.reporttype == "liver report"):
                liver[x.reportKey] = x.reportValue  
            elif(x.reporttype == "stool report"):
                stool[x.reportKey] = x.reportValue  

        dl3['blood']=blood
        dl3['urine']=urine
        dl3['liver']=liver
        dl3['stool']=stool

        response_json['comment'] = ReportString.objects.get(reportID=reportID).comments
        response_json['summary'] = ReportString.objects.get(reportID=reportID).summary

        response_json['list'] = dl1

        response_json['basic'] = dl2
        response_json['report_value'] = dl3
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"
    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def sendReportOCR(request):

    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        reportID = str(request.POST.get("reportID"))
        reportfault = str(request.POST.get("status"))
        
        if(reportfault == "True"):
            message = 'OCR Mismatch for ' + reportID + '. Please verify.'
            sendMail('OCR Mismatch',message,"vijeyanidhi@gmail.com")
        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"
    print (str(response_json))
    return JsonResponse(response_json)
