# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class TermDataAdmin(admin.ModelAdmin):
    list_display = ["termName","modified","created"]
    search_fields = ["termName","modified","created"]

admin.site.register(TermData, TermDataAdmin)

class ReportStringAdmin(admin.ModelAdmin):
    list_display = ["reportID","comments","summary","modified","created"]
    search_fields = ["reportID","comments","summary","modified","created"]

admin.site.register(ReportString, ReportStringAdmin)

class ReportValuesAdmin(admin.ModelAdmin):
    list_display = ["reportID","reporttype","reportKey","reportValue","modified","created"]
    search_fields = ["reportID","reporttype","reportKey","reportValue","modified","created"]

admin.site.register(ReportValues, ReportValuesAdmin)

class ReportBasicAdmin(admin.ModelAdmin):
    list_display = ["reportID","reportKey","reportValue","modified","created"]
    search_fields = ["reportID","reportKey","reportValue","modified","created"]

admin.site.register(ReportBasic, ReportBasicAdmin)

class ReportListAdmin(admin.ModelAdmin):
    list_display = ["reportID","reportKey","reportValue","modified","created"]
    search_fields = ["reportID","reportKey","reportValue","modified","created"]

admin.site.register(ReportList, ReportListAdmin)

