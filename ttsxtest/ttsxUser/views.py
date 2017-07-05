#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.


def ttsx_zhuce(request):
    content = {'key_zd':'注册'}
    return render(request, 'ttsxUser/register.html', content)


def index(request):
    return render(request, 'ttsxUser/index.html')


def ttsx_dengluz(request):
    user = request.POST
    name = user.get('user_name')
    pwd = user.get('pwd')
    email = user.get('email')
    userInfo = UserInfo()
    userInfo.user_name = name
    userInfo.user_pwd = pwd
    userInfo.user_email = email
    userInfo.save()
    content = {'key_zd':'登陆'}
    return render(request, 'ttsxUser/login.html', content)


def ttsx_denglud(request):
    content = {'key_zd':'登陆'}
    return render(request, 'ttsxUser/login.html', content)