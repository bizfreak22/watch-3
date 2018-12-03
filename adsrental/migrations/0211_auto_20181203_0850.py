# Generated by Django 2.1.3 on 2018-12-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0210_auto_20181130_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadaccount',
            name='ban_reason',
            field=models.CharField(blank=True, choices=[('Google - Policy', 'Google - Policy'), ('Google - Billing', 'Google - Billing'), ('Google - Unresponsive User', 'Google - Unresponsive User'), ('Facebook - Policy', 'Facebook - Policy'), ('Facebook - Suspicious', 'Facebook - Suspicious'), ('Facebook - Lockout', 'Facebook - Lockout'), ('Facebook - Unresponsive User', 'Facebook - Unresponsive User'), ('Duplicate', 'Duplicate'), ('Bad ad account', 'Bad ad account'), ('auto_offline', 'Auto: offline for 2 weeks'), ('auto_wrong_password', 'Auto: wrong password for 2 weeks'), ('auto_checkpoint', 'Auto: reported security checkpoint for 2 weeks'), ('auto_not_used', 'Auto: not used for 2 weeks after delivery'), ('ADSDB', 'Banned by Adsdb sync'), ('Other', 'Other')], help_text='Populated from ban form', max_length=50, null=True),
        ),
    ]
