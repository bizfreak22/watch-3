from __future__ import unicode_literals

from django.db import models


class LeadChange(models.Model):
    lead = models.ForeignKey('adsrental.Lead')
    field = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)