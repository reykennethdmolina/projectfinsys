from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime


# Create your models here.
class Wtax(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=250)
    rate = models.IntegerField(default=0)
    wtaxtype_id = models.IntegerField(default=0)
    chartofaccount = models.ForeignKey('chartofaccount.Chartofaccount', default=0, related_name='wtaxchartofaccount_id',
                                       validators=[MinValueValidator(1)])
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('C', 'Cancelled'),
        ('O', 'Posted'),
        ('P', 'Printed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    enterby = models.ForeignKey(User, default=1, related_name='wtax_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='wtax_modify')
    modifydate = models.DateTimeField(default=datetime.datetime.now())
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'wtax'
        ordering = ['-pk']
        permissions = (("view_wtax", "Can view wtax"),)

    def get_absolute_url(self):
        return reverse('wtax:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def status_verbose(self):
        return dict(Wtax.STATUS_CHOICES)[self.status]


