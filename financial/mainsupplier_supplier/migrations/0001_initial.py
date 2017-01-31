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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsupplier', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainsupplier_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 26, 8, 2, 1, 633000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mainsupplier_supplier_enter', to=settings.AUTH_USER_MODEL)),
                ('mainsupplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainsupplier_id', to='mainsupplier.Mainsupplier', validators=[django.core.validators.MinValueValidator(1)])),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mainsupplier_supplier_modify', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_id', to='supplier.Supplier', validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'mainsupplier_supplier',
                'permissions': (('view_mainsupplier_supplier', 'Can view mainsupplier_supplier'),),
            },
        ),
        migrations.AlterUniqueTogether(
            name='mainsupplier_supplier',
            unique_together=set([('mainsupplier', 'supplier')]),
        ),
    ]
