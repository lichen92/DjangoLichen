#coding=utf-8
from django.shortcuts import render,redirect
from models import *
import hashlib
from django.http import JsonResponse
import datetime
from ttsx_goods.models import *
# Create your views here.



def yanzheng(func):
    context = {}
    def f1(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            # print request.session.has_key('user_id')
            return func(request,*args,**kwargs)
        else:
            return redirect('/user/login/')
    return f1
def ttsx_zhuce(request):
    context = {'title':'注册', 'num':'0'}
    return render(request, 'ttsxUser/register.html', context)


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
            request.session['user_id'] = users[0].id
            request.session['user_name'] = username
            request.session.set_expiry(0)
            # print '============'
            # print request.session['url_path']
            # print '============'
            response = redirect(request.session['url_path'])#request.session['url_path']
            if uname_jz == '1':
                response.set_cookie('username', username, expires=datetime.datetime.now()+datetime.timedelta(days = 7))
            else:
                response.set_cookie('username', '', max_age=-1)
            return response
        else:
            context['pwd_erro'] = '1'
            return render(request, 'ttsxUser/login.html', context)


def islogin(request):
    if request.session.has_key('user_id'):
        return JsonResponse({'gnum':1})
    else:
        return JsonResponse({'gnum':0})


def logout(request):
    request.session.set_expiry(-1)
    return redirect('/user/login')


@yanzheng
def center(request):
    goods_id = request.COOKIES.get('goods_id')
    id_list = goods_id.split(',')
    # print goods_list
    goods_list = []
    for id1 in id_list:
        print id1
        print GoodsInfo
        goods = GoodsInfo.objects.get(id=id1)
        goods_list.append(goods)
    user = UserInfo.objects.get(id=request.session['user_id'])
    context = {'title': '用户中心', 'user':user,'goods_list':goods_list}
    return render(request, 'ttsxUser/center.html', context)


@yanzheng
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    context = {'title': '用户中心', 'user':user}
    if request.method == 'POST':
        post = request.POST
        user.user_sjr = post.get('user_sjr')
        user.user_addr = post.get('user_addr')
        user.user_postcode = post.get('user_postcode')
        user.user_phone_number = post.get('user_phonenumber')
        user.save()
    return render(request, 'ttsxUser/site.html', context)


@yanzheng
def order(request):
    context = {'title': '用户中心'}
    return render(request, 'ttsxUser/order.html', context)


def cart(request):
    context = {}
    return render(request,'ttsxUser/cart.html',context)
