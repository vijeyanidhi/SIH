# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class LoginDataAdmin(admin.ModelAdmin):
    list_display = ["ident","password","otp","flag","modified","created"]
    search_fields = ["ident","password","modified","created"]

admin.site.register(LoginData, LoginDataAdmin)

