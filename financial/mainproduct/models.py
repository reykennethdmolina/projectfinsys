from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Mainproduct(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=250)
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('C', 'Cancelled'),
        ('O', 'Posted'),
        ('P', 'Printed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    enterby = models.ForeignKey(User, default=1, related_name='mainproduct_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='mainproduct_modify')
    modifydate = models.DateTimeField(default=datetime.datetime.now())
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'mainproduct'
        ordering = ['-pk']
        permissions = (("view_mainproduct", "Can view mainproduct"),)

    def get_absolute_url(self):
        return reverse('mainproduct:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.code

    def status_verbose(self):
        return dict(Mainproduct.STATUS_CHOICES)[self.status]