# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-30 06:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170130_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 14, 49, 2, 32000)),
        ),
    ]