# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 00:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainunit', '0002_auto_20170124_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainunit',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 26, 8, 2, 1, 529000)),
        ),
    ]
