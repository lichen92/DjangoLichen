#coding=utf-8
from django.shortcuts import render,redirect
from models import *
import hashlib
from django.http import JsonResponse
import datetime
# Create your views here.


def ttsx_zhuce(request):
    context = {'title':'注册', 'num':'0'}
    return render(request, 'ttsxUser/register.html', context)


def index(request):
    context = {'num_index':'2', 'num':'0'}
    return render(request, 'ttsxUser/index.html', context)


def ttsx_dengluz(request):
    user = request.POST
    name = user.get('user_name')
    pwd = user.get('pwd')
    email = user.get('email')
    pwd_sha1 = hashlib.sha1(pwd).hexdigest()
    userInfo = UserInfo()
    userInfo.user_name = name
    userInfo.user_pwd = pwd_sha1
    userInfo.user_email = email
    userInfo.save()
    context = {'title':'登陆', 'num':'0'}
    return render(request, 'ttsxUser/login.html', context)


def ttsx_denglud(request):
    name = request.COOKIES.get('username','')
    context = {'title':'登陆', 'name':name, 'num':'0'}
    return render(request, 'ttsxUser/login.html', context)


def register_valid(request):
    name = request.GET.get('name')
    name_num = UserInfo.objects.filter(user_name=name).count()
    context = {'name_num':name_num}
    return  JsonResponse(context)


def login_handle(request):
    #接受request中传输过来的数值：用户名及密码
    post01 = request.POST
    username = post01.get('username')
    pwd = post01.get('pwd')
    uname_jz = post01.get('name_jz', '0')
    #将密码采用sha1加密
    pwd_sha1 = hashlib.sha1(pwd).hexdigest()
    #夺取对象及其中的数据
    context = {'key_zd': '登陆', 'name':username, 'pwd':pwd}
    users = UserInfo.objects.filter(user_name=username)
    if len(users) == 0:
        context['name_erro'] = '1'
        return render(request, 'ttsxUser/login.html',context)
    else:
        if users[0].user_pwd == pwd_sha1:#登陆成功
            response = redirect('/user/')
            if uname_jz == '1':
                response.set_cookie('username', username, expires=datetime.datetime.now()+datetime.timedelta(days = 7))
            else:
                response.set_cookie('username', '', max_age=-1)
            return response
        else:
            context['pwd_erro'] = '1'
            return render(request, 'ttsxUser/login.html', context)


def center(request):
    context = {'title': '用户中心'}
    return render(request, 'ttsxUser/center.html', context)


def site(request):
    context = {'title': '用户中心'}
    return render(request, 'ttsxUser/site.html', context)


def order(request):
    context = {'title': '用户中心'}
    return render(request, 'ttsxUser/order.html', context)

