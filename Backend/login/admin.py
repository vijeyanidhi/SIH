# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class LoginDataAdmin(admin.ModelAdmin):
    list_display = ["ident","password","accessLevel","modified","created"]
    search_fields = ["ident","password","accessLevel","modified","created"]

admin.site.register(LoginData, LoginDataAdmin)

class ResetDataAdmin(admin.ModelAdmin):
    list_display = ["ident","name","emailID","mobile","modified","created"]
    search_fields = ["ident","name","emailID","mobile","modified","created"]

admin.site.register(ResetData, ResetDataAdmin)

class OTPDataAdmin(admin.ModelAdmin):
    list_display = ["emailID","otp","flag","stop","modified","created"]
    search_fields = ["emailID","modified","created"]

admin.site.register(OTPData, OTPDataAdmin)
