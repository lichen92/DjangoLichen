from django.db import models
from ttsx_goods.models import GoodsInfo
# Create your models here.


class CartInfo(models.Model):
    user = models.ForeignKey('ttsxUser.UserInfo')
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()