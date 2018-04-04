# Generated by Django 2.0.3 on 2018-04-04 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0112_leadaccount_security_checkpoint_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadOnlyLeadAccount',
            fields=[
            ],
            options={
                'verbose_name': 'Read-only Lead Account',
                'verbose_name_plural': 'Read-only Lead Accounts',
                'proxy': True,
                'indexes': [],
            },
            bases=('adsrental.leadaccount',),
        ),
    ]
