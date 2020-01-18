"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from login.views import *
from report.views import *
from info.views import *

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainPage),
    url(r'^login1/', login),
    url(r'^signup/',renderSignUp),
    url(r'^verifymail/',verifymail),
    url(r'^verifyotp/',verifyotp),
    url(r'^option/',renderOption),
    url(r'^inpcustomer/',renderInpCustomer),
    url(r'^inpdoctor/',renderInpDoctor),
    url(r'^inpchecker/',renderInpChecker),
    url(r'^signin/',signin),
    url(r'^custprofile/',custprofile),
    url(r'^docprofile/',docprofile),
    url(r'^checkerprofile/',checkerprofile),
    url(r'^custinfo/',info),
    url(r'^customer/',customer),
    url(r'^doctor/',doctor),
    url(r'^upload/',upload),
    url(r'^detail/',detail),
    url(r'^getrep/',sendReportID),
    url(r'^getreplistvalues/',sendReportListvalues),
    url(r'^getrepbasicvalues/',sendReportBasicvalues),
    url(r'^getrepvalues/',sendReportvalues),
    url(r'^getrepstring/',sendReportStrings),
    url(r'^getReportTotal/',sendTotalReport)
]
