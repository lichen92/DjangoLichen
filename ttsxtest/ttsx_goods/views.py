#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.core.paginator import Paginator
from datetime import date
from haystack.generic_views import SearchView
# Create your views here.


class MySearchView(SearchView):

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['num_index'] = "1"
        page_range = []
        page = context.get('page_obj')
        if page.number <= 2:
            page_range = range(1,6)
        elif page.number >= page.paginator.num_pages-1:
            page_range = range(page.paginator.num_pages-4,page.paginator.num_pages+1)
        else:
            page_range = range(page.number-2,page.number+3)

        context['page_range'] = page_range

        return context


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


def list(request,num1,pindex,num2):#num1和pindex是非int类型
    try:
        str = '-id'
        desc = request.GET.get('desc','1')
        if int(num2)==2:
                if desc == '1':
                    str = 'gprice'
                else:
                    str = '-gprice'
        if int(num2)==3:
            str = 'gclick'
        t1 = TypeInfo.objects.get(id=num1)
        new_list = t1.goodsinfo_set.order_by('-id')[0:2]
        glist = t1.goodsinfo_set.order_by(str)
        paginator = Paginator(glist, 3)
        pindex_int = int(pindex)
        if pindex_int<1:
            pindex_int=1
        if pindex_int>paginator.num_pages:
            pindex_int=paginator.num_pages
        page = paginator.page(pindex_int)
        context = {'desc':desc, 'num_index':'2', 'num2': int(num2), 't1':t1, 'new_list':new_list,'page':page,'paginator':paginator}
        return render(request,'ttsx_goods/list.html',context)
    except:
        return redirect(request,'404.html')


def detail(request, id):
    goods = GoodsInfo.objects.get(pk=int(id))
    new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'num_index':'2', 'title':'详情介绍', 'goods':goods, 'new_list':new_list}
    response = render(request, 'ttsx_goods/detail.html', context)
    gids = request.COOKIES.get('goods_id', '').split(',')
    kong = ''
    if kong in gids:
        gids.remove(kong)
    if str(id) not in gids:
        gids.insert(0, str(id))
    if str(id) in gids:
        gids.remove(id)
        gids.insert(0, str(id))
    if len(gids) > 5:
        gids.pop()
    response.set_cookie('goods_id', ','.join(gids), max_age=60*60*24*7)
    return response



