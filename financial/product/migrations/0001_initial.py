# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-24 02:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainproduct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('pagecount', models.IntegerField(default=0)),
                ('cmsgroup_id', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 24, 10, 6, 25, 486191))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_enter', to=settings.AUTH_USER_MODEL)),
                ('mainproduct', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='mainproduct_id', to='mainproduct.Mainproduct', validators=[django.core.validators.MinValueValidator(1)])),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'product',
                'permissions': (('view_product', 'Can view product'),),
            },
        ),
    ]
