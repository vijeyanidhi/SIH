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

class ReportString(models.Model):
    reportID = models.CharField(max_length=240, blank=False, null=True)
    comments = models.CharField(max_length=240, blank=False, null=True)
    summary = models.CharField(max_length=240, blank=False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return str(self.reportID)

class ReportValues(models.Model):
    reportID = models.ForeignKey(ReportString, null=True,on_delete=models.PROTECT)
    reporttype = models.CharField(max_length=240, blank=False, null=True)
    reportKey = models.CharField(max_length=240, blank=False, null=True)
    reportValue = models.CharField(max_length=240, blank=False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class ReportBasic(models.Model):
    reportID = models.ForeignKey(ReportString, null=True,on_delete=models.PROTECT)
    reportKey = models.CharField(max_length=240, blank=False, null=True)
    reportValue = models.CharField(max_length=240, blank=False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class ReportList(models.Model):
    reportID = models.ForeignKey(ReportString, null=True,on_delete=models.PROTECT)
    reportKey = models.CharField(max_length=240, blank=False, null=True)
    reportValue = models.CharField(max_length=240, blank=False, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
