# Generated by Django 2.0.6 on 2018-07-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0172_leadchange_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadhistorymonth',
            name='move_to_next_month',
            field=models.BooleanField(default=False),
        ),
    ]
