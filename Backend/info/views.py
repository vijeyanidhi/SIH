# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *

# Create your views here.

@csrf_exempt
def signup(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        password = str(request.POST.get("password"))
        accessLevel = str(request.POST.get("accessLevel"))  #customer, doctor,checker
        name = str(request.POST.get("name"))
        emailID = str(request.POST.get("emailID"))
        mobile = str(request.POST.get("mobile"))
        houseNumber = str(request.POST.get("houseNumber"))
        streetName = str(request.POST.get("streetName"))
        area = str(request.POST.get("area"))
        city = str(request.POST.get("city"))
        state = str(request.POST.get("state"))
        country = str(request.POST.get("country"))

        OTPDataInstance = OTPData.objects.get(emailID=emailID)

        if(not OTPDataInstance.flag):
            print("Not verified") # mark1
        loginrow = LoginData.objects.create(password = password,accessLevel = accessLevel)
        loginrow.save()

        resetrow = ResetData.objects.create(ident = loginrow, name = name, emailID = emailID, mobile = mobile)
        resetrow.save()

        if accessLevel == "customer":
            customerrow = CustomerData.objects.create(ident = loginrow, houseNumber = houseNumber, streetName = streetName, area = area, city = city, state = state, country = country)
            customerrow.save()
        elif accessLevel == "doctor":
            doctorrow = DoctorData.objects.create(ident = loginrow, houseNumber = houseNumber, streetName = streetName, area = area, city = city, state = state, country = country)
            doctorrow.save()
        elif accessLevel == "checker":
            checkerrow = CheckerData.objects.create(ident = loginrow, houseNumber = houseNumber, streetName = streetName, area = area, city = city, state = state, country = country)
            checkerrow.save()
        else:
            print(name)
            print("error wrong access Level entered")
        response_json['success'] = True
        response_json['message'] = 'Successful'
        # response_json['ident'] = loginrow
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)


@csrf_exempt
def update(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
        identInstance = LoginData.objects.get(ident=ident)
        accessLevel = identInstance.accessLevel
        name = str(request.POST.get("name"))
        emailID = str(request.POST.get("emailID"))
        mobile = str(request.POST.get("mobile"))
        houseNumber = str(request.POST.get("houseNumber"))
        streetName = str(request.POST.get("streetName"))
        area = str(request.POST.get("area"))
        city = str(request.POST.get("city"))
        state = str(request.POST.get("state"))
        country = str(request.POST.get("country"))
        
        resetrow = ResetData.objects.get(ident = identInstance)
        resetrow.save()

        setattr(resetrow,'name',name)
        setattr(resetrow,'emailID',emailID)
        setattr(resetrow,'mobile',mobile)

        if accessLevel == "customer":
            row = CustomerData.objects.get(ident = loginrow)
            isCustomer = str(request.POST.get("isCustomer"))
            setattr(row,'isCustomer',isCustomer)
        elif accessLevel == "doctor":
            row = DoctorData.objects.get(ident = loginrow)
            medicalLicenseNumber = str(request.POST.get("medicalLicenseNumber"))
            hospitalName = str(request.POST.get("hospitalName"))
            speciality = str(request.POST.get("speciality"))
            setattr(row,'medicalLicenseNumber',medicalLicenseNumber)
            setattr(row,'hospitalName',hospitalName)
            setattr(row,'speciality',speciality)
        elif accessLevel == "checker":
            row = CheckerData.objects.get(ident = loginrow)

        setattr(row,'houseNumber',houseNumber)
        setattr(row,'streetName',streetName)
        setattr(row,'area',area)
        setattr(row,'city',city)
        setattr(row,'state',state)
        setattr(row,'country',country)
        row.save()

        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)

@csrf_exempt
def info(request):
    response_json = {}
    if request.method == 'POST':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        ident = str(request.POST.get("ident"))
        identInstance = LoginData.objects.get(ident=ident)
        accessLevel = identInstance.accessLevel

        response_json['accessLevel'] = accessLevel

        ResetDataInstance = ResetData.objects.get(ident=identInstance)

        response_json['name'] = ResetDataInstance.name
        response_json['emailID'] = ResetDataInstance.emailID
        response_json['mobile'] = ResetDataInstance.mobileResetDataInstance

        if accessLevel == "customer":
            row = CustomerData.objects.get(ident = identInstance)
            response_json['isCustomer'] = row.isCustomer
        elif accessLevel == "doctor":
            row = DoctorData.objects.get(ident = identInstance)
            response_json['medicalLicenseNumber'] = row.medicalLicenseNumber
            response_json['hospitalName'] = row.hospitalName
            response_json['speciality'] = row.speciality
        elif accessLevel == "checker":
            row = CheckerData.objects.get(ident = identInstance)
            response_json['totalCleared'] = row.totalCleared  # display only no edit
            response_json['failure'] = row.failure            # display only no edit
 
        response_json['houseNumber'] = row.houseNumber
        response_json['streetName'] = row.streetName
        response_json['area'] = row.area
        response_json['city'] = row.city
        response_json['state'] = row.state
        response_json['country'] = row.country

        response_json['success'] = True
        response_json['message'] = 'Successful'
    else:
        response_json['success'] = False
        response_json['message'] = "Not Post Method"

    print (str(response_json))
    return JsonResponse(response_json)
