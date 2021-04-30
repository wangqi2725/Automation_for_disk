"""Automation_management_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path,include
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #主页，登录，注册，登出
    #index,login,register,logout
    #1.未登录人员，全部先到login界面
    #2.已登录，访问login跳转index
    #3.已登出，访问register先logout
    #4.logout，跳转login
    # path('index/',views.index),
    # path('login/',views.login),
    # path('register/',views.register),
    # path('logout/',views.logout),


    #cmdn
    path('assets/',include('app.urls'))

]
