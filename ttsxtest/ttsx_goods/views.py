#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    type_list = TypeInfo.objects.all()
    # print type_list
    plist = []
    for type1 in type_list:
        # print type1.goodsinfo_set.order_by('-id')[0:3]
        # print '='*30
        new_list = type1.goodsinfo_set.order_by('-id')[0:3]
        # print '=' * 30
        # print new_list
        hot_list = type1.goodsinfo_set.order_by('-gclick')[0:4]
        plist.append({'type1':type1, 'new_list':new_list, 'hot_list':hot_list})
    context = {'num_index':'2', 'title':'首页', 'plist':plist}
    return render(request, 'ttsx_goods/index.html', context)


def list(request,num1,pindex):#num1和pindex是非int类型
    t1 = TypeInfo.objects.get(id=num1)
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by('-id')
    paginator = Paginator(glist, 15)
    pindex_int = int(pindex)
    if pindex_int<1:
        pindex_int=1
    if pindex_int>paginator.num_pages:
        pindex_int=paginator.num_pages
    page = paginator.page(pindex_int)
    context = {'num_index':'2', 't1':t1, 'new_list':new_list,'page':page,'paginator':paginator}
    return render(request,'ttsx_goods/list.html',context)


def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'num_index':'2', 'title':'详情介绍', 'goods':goods, 'new_list':new_list}
    return render(request, 'ttsx_goods/detail.html', context)