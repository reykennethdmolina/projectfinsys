# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-24 02:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customertype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 24, 10, 16, 17, 979735)),
        ),
    ]
