# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import *

# Create your models here.

class TermData(models.Model):
    termName = models.CharField(max_length=240, blank=False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return str(self.termName)

class Report(models.Model):
    reportID = models.CharField(max_length=240, blank=False, null=True)
    customerIdent = models.ForeignKey(LoginData)
    doctorName = models.CharField(max_length=240, blank=False, null=True)
    doctorIdent = models.CharField(LoginData)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class ReportContent(models.Model):
    termName = models.ForeignKey(TermData, null=True)
    value = models.CharField(max_length=240, blank=False, null=True)
    units = models.CharField(max_length=240, blank=False, null=True)
    refValue = models.CharField(max_length=240, blank = False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
