# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-15 20:45
from __future__ import unicode_literals

import adsrental.models.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0023_auto_20180112_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerIOEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('shipped', 'Shipped'), ('delivered', 'Delivered'), ('offline', 'Offline'), ('lead_approved', 'Approved')], max_length=255)),
                ('kwargs', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            bases=(models.Model, adsrental.models.mixins.FulltextSearchMixin),
        ),
    ]
