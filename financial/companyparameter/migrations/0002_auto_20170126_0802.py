# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 00:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyparameter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyparameter',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 26, 8, 2, 1, 639000)),
        ),
    ]