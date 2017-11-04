# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0009_raspberrypi_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='activation_ip_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='ad_account_status_last_checked',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='banned_reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='billed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='converted_account_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='converted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='credentials_acquired',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='email_bounced_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='geocode_accuracy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='industry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='is_converted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lead',
            name='is_deleted',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='jigsaw',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='jigsaw_contact_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='last_referenced_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='last_touch_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='lastname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='middlename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='not_banned_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='old_pi_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='payment_first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='postal_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='rating',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='registered_isp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='salesforce_id',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='secret_changed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='winprox_download_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='winprox_online',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='winprox_tunnel_last_started',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='annual_revenue',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='facebook_account',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lead',
            name='facebook_account_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='facebook_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='facebook_friends',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='facebook_secret',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='google_account',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lead',
            name='google_account_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
