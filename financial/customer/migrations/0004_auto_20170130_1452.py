# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-30 06:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20170126_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 14, 52, 5, 399000)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
