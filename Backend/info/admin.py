# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ["ident","houseNumber","streetName","area","city","state","country","isCustomer","modified","created"]
    search_fields = ["ident","houseNumber","streetName","area","city","state","country","isCustomer","modified","created"]

admin.site.register(CustomerData, CustomerDataAdmin)

class DoctorDataAdmin(admin.ModelAdmin):
    list_display = ["ident","houseNumber","streetName","area","city","state","country","medicalLicenseNumber","hospitalName","speciality","modified","created"]
    search_fields = ["ident","houseNumber","streetName","area","city","state","country","medicalLicenseNumber","hospitalName","speciality","modified","created"]

admin.site.register(DoctorData, DoctorDataAdmin)

class CheckerDataAdmin(admin.ModelAdmin):
    list_display = ["ident","houseNumber","streetName","area","city","state","country","totalCleared","failure","modified","created"]
    search_fields = ["ident","houseNumber","streetName","area","city","state","country","totalCleared","failure","modified","created"]

admin.site.register(CheckerData, CheckerDataAdmin)

class customerDoctorAdmin(admin.ModelAdmin):
    list_display = ["ident","Doctor","modified","created"]
    search_fields = ["ident","Doctor","modified","created"]

admin.site.register(customerDoctor, customerDoctorAdmin)



