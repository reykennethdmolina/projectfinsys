# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 00:02
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serviceclassification', '0003_auto_20170126_0802'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Serviceinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precode', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('code', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('description', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 26, 8, 2, 1, 626000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='serviceinformation_enter', to=settings.AUTH_USER_MODEL)),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='serviceinformation_modify', to=settings.AUTH_USER_MODEL)),
                ('serviceclassification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceclassification_id', to='serviceclassification.Serviceclassification', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)])),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'serviceinformation',
                'permissions': (('view_serviceinformation', 'Can view serviceinformation'),),
            },
        ),
    ]
