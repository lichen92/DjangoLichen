from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=40)
    user_email = models.CharField(max_length=20)
    user_sjr = models.CharField(default='', max_length=10)
    user_addr = models.CharField(default='', max_length=100)
    user_postcode = models.CharField(default='', max_length=6)
    user_phone_number = models.CharField(default='', max_length=11)


