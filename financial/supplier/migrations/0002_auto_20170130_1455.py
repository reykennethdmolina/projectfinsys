# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-30 06:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 14, 55, 50, 445000)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='tin',
            field=models.CharField(max_length=20),
        ),
    ]
