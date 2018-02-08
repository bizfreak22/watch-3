# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-08 05:18
from __future__ import unicode_literals

import base64

from django.db import migrations, models


def decode_fb_fields(apps, schema_editor):
    Lead = apps.get_model('adsrental', 'Lead')
    for lead in Lead.objects.filter(fb_email__isnull=False):
        if '@' not in lead.fb_email:
            try:
                lead.fb_email = base64.b64decode(lead.fb_email)
                lead.fb_secret = base64.b64decode(lead.fb_secret)
                lead.save()
            except Exception as e:
                print lead.email, e, lead.fb_email, lead.fb_secret


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0064_lead_wrong_password_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='google_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='google_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
