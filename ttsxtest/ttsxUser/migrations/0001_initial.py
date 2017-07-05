# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pwd', models.CharField(max_length=40)),
                ('user_email', models.CharField(max_length=20)),
                ('user_sjr', models.CharField(default=b'', max_length=10)),
                ('user_addr', models.CharField(default=b'', max_length=100)),
                ('user_postcode', models.CharField(default=b'', max_length=6)),
                ('user_phone_number', models.CharField(default=b'', max_length=11)),
            ],
        ),
    ]
