# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-12 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0071_remove_ec2instance_web_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='ec2instance',
            name='tunnel_up_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
