# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-30 08:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20170130_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contactperson',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='contactposition',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 16, 36, 17, 294000)),
        ),
    ]
