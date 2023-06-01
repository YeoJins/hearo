"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls), #관리자페이지
    path('home/', include('home.urls')), #기능 선택
    path('', main, name="main"), #완전 메인화면(첫화면)
    path('users/', include('users.urls')), #로그인, 회원가입
    path('mic/', include('mic.urls'), name='mic'),
    path('camera/', include('camera.urls'), name='cam'),
]
