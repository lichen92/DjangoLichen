from django.shortcuts import render
from django.http import JsonResponse
from .models import CartInfo
# Create your views here.


def cart_add(request):
    try:
        cart = CartInfo()
        user_id = request.session.get('user_id')
        gid = request.GET.get('gid')
        count = int(request.GET.get('count',1))
        carts = CartInfo.objects.filter(user_id = int(user_id), goods_id = int(gid))
        if len(carts)==1:
            count +=count
            cart.count=count
            cart.save()
        else:
            cart.user_id = int(user_id)
            cart.goods_id = int(gid)
            cart.count = count
            cart.save()
        return JsonResponse({'isadd': 1})
    except:
        return JsonResponse({'isadd': 0})
