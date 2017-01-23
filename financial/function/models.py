from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
import datetime


class Function(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=250)
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('C', 'Cancelled'),
        ('O', 'Posted'),
        ('P', 'Printed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    enterby = models.ForeignKey(User, default=1, related_name='function_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='function_modify')
    modifydate = models.DateTimeField(default=datetime.datetime.now())
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'function'
        ordering = ['-pk']
        permissions = (("view_function", "Can view function"),)

    def get_absolute_url(self):
        return reverse('function:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def status_verbose(self):
        return dict(Function.STATUS_CHOICES)[self.status]
