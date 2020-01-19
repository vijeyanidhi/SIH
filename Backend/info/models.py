# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import *

# Create your models here.

class CustomerData(models.Model):
    ident = models.ForeignKey(LoginData, null=True,on_delete=models.PROTECT)
    houseNumber = models.CharField(max_length=240, blank=False, null=True)
    streetName = models.CharField(max_length=240, blank=False, null=True)
    area = models.CharField(max_length=240, blank=False, null=True)
    city = models.CharField(max_length=240, blank=False, null=True)
    state = models.CharField(max_length=240, blank=False, null=True)
    country = models.CharField(max_length=240, blank=False, null=True)
    isCustomer = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class DoctorData(models.Model):
    ident = models.ForeignKey(LoginData, null=True,on_delete=models.PROTECT)
    houseNumber = models.CharField(max_length=240, blank=False, null=True)
    streetName = models.CharField(max_length=240, blank=False, null=True)
    area = models.CharField(max_length=240, blank=False, null=True)
    city = models.CharField(max_length=240, blank=False, null=True)
    state = models.CharField(max_length=240, blank=False, null=True)
    country = models.CharField(max_length=240, blank=False, null=True)
    medicalLicenseNumber = models.CharField(max_length=240, blank=False, null=True)
    hospitalName = models.CharField(max_length=240, blank=False, null=True)
    speciality = models.CharField(max_length=240, blank=False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class CheckerData(models.Model):
    ident = models.ForeignKey(LoginData, null=True,on_delete=models.PROTECT)
    houseNumber = models.CharField(max_length=240, blank=False, null=True)
    streetName = models.CharField(max_length=240, blank=False, null=True)
    area = models.CharField(max_length=240, blank=False, null=True)
    city = models.CharField(max_length=240, blank=False, null=True)
    state = models.CharField(max_length=240, blank=False, null=True)
    country = models.CharField(max_length=240, blank=False, null=True)
    totalCleared = models.IntegerField(default=0)
    failure = models.IntegerField(default=0)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class customerDoctor(models.Model):
    ident = models.ForeignKey(LoginData, null=True,on_delete=models.PROTECT)
    Doctor = models.ForeignKey(DoctorData, null=True,on_delete=models.PROTECT)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
