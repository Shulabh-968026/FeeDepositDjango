"""feemanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login),
    path('logacc/',logacc),
    path('adminhome/',adminhome),
    path('addaccountant/',addaccountant),
    path('logout/',logout),
    path('accountanthome/',accountanthome),
    path('addstudent/',addstudent),
    path('viewaccountant/',viewaccountant),
    path('viewstudent/',viewstudent),
    path('searchstudent/',searchstudent),
    path('duefee/',duefee),
    path('editaccountant/',editaccountant),
    path('deleteaccountant/',deleteaccountant),
    path('delaccountant/',delaccountant),
    path('editacc/',editacc),
    path('editstudent/',editstudent),
    path('editstud/',editstud),
    path('deletestudent/',deletestudent),
    path('delstudent/',delstudent),
]
