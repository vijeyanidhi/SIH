# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class TermDataAdmin(admin.ModelAdmin):
    list_display = ["termName","modified","created"]
    search_fields = ["termName","modified","created"]

admin.site.register(TermData, TermDataAdmin)



class ReportAdmin(admin.ModelAdmin):
    list_display = ["reportID","customerIdent","doctorName","modified","created"]
    search_fields = ["reportID","customerIdent","doctorName,"modified","created"]

admin.site.register(Report, ReportAdmin)

class ReportContentAdmin(admin.ModelAdmin):
    list_display = ["ReportID","termName","value","units","refValue","modified","created"]
    search_fields = ["ReportID","modified","created"]

admin.site.register(ReportContent, ReportContentAdmin)

