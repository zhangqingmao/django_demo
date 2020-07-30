"""django_demo URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from TestModel import testdb

urlpatterns = [
    url(r'^$', testdb.testdb),
    url(r'^admin/', admin.site.urls),        #admin后台路由
    path('testdb/', testdb.testdb),
    path('index/login/',testdb.login),
    path('login/zc/',testdb.zc),
    path('index/',testdb.index),
    path('login/sms/',testdb.sendSms)
]
