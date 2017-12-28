from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

from adsrental.models.raspberry_pi import RaspberryPi

# from salesforce_handler.models import Lead as SFLead


class Lead(models.Model):
    STATUS_QUALIFIED = 'Qualified'
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Banned', 'Banned'),
        (STATUS_QUALIFIED, 'Qualified'),
        ('In-Progress', 'In-Progress'),
    ]

    leadid = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='Available')
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    usps_tracking_code = models.CharField(max_length=255, blank=True, null=True)
    utm_source = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    google_account = models.BooleanField(default=False)
    facebook_account = models.BooleanField(default=False)
    raspberry_pi = models.ForeignKey('adsrental.RaspberryPi', null=True, blank=True, default=None)
    wrong_password = models.BooleanField(default=False)
    bundler_paid = models.BooleanField(default=False)
    pi_delivered = models.BooleanField(default=False)
    tested = models.BooleanField(default=False)
    facebook_account_status = models.CharField(max_length=255, choices=[('Available', 'Available'), ('Banned', 'Banned')], blank=True, null=True)
    google_account_status = models.CharField(max_length=255, choices=[('Available', 'Available'), ('Banned', 'Banned')], blank=True, null=True)
    fb_email = models.CharField(max_length=255, blank=True, null=True)
    fb_secret = models.CharField(max_length=255, blank=True, null=True)
    is_sync_adsdb = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pi_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.leadid

    class Meta:
        db_table = 'lead'

    def get_pi_sent_this_month(self):
        if not self.pi_sent:
            return False
        now = timezone.now()
        if now.year == self.pi_sent.year and now.month == self.pi_sent.month:
            return True

        return False

    @staticmethod
    def upsert_from_sf(sf_lead, lead):
        raspberry_pi = None
        if sf_lead.raspberry_pi:
            old_raspberry_pi = lead.raspberry_pi if lead else None
            if sf_lead.raspberry_pi and not old_raspberry_pi:
                old_raspberry_pi = RaspberryPi.objects.filter(rpid=sf_lead.raspberry_pi.name).first()

            if sf_lead.raspberry_pi and old_raspberry_pi and sf_lead.raspberry_pi.name != old_raspberry_pi.rpid:
                old_raspberry_pi = RaspberryPi.objects.filter(rpid=sf_lead.raspberry_pi.name).first()

            raspberry_pi = RaspberryPi.upsert_from_sf(sf_lead.id, sf_lead.raspberry_pi, old_raspberry_pi)

        if lead is None:
            lead = Lead(
                leadid=sf_lead.id,
            )

        address = ', '.join([
            sf_lead.street or '',
            sf_lead.city or '',
            sf_lead.state or '',
            sf_lead.postal_code or '',
            sf_lead.country or '',
        ])

        for new_field, old_field in (
            (sf_lead.first_name, lead.first_name, ),
            (sf_lead.last_name, lead.last_name, ),
            (sf_lead.email, lead.email, ),
            (sf_lead.phone, lead.phone, ),
            (address, lead.address, ),
            (sf_lead.account_name, lead.account_name, ),
            (sf_lead.status, lead.status, ),
            (sf_lead.raspberry_pi.usps_tracking_code if sf_lead.raspberry_pi else None, lead.usps_tracking_code, ),
            (sf_lead.utm_source, lead.utm_source, ),
            (sf_lead.google_account, lead.google_account, ),
            (raspberry_pi.pk if raspberry_pi else None, lead.raspberry_pi.pk if lead.raspberry_pi else None, ),
            (sf_lead.wrong_password, lead.wrong_password, ),
            (sf_lead.bundler_paid, lead.bundler_paid, ),
            (sf_lead.raspberry_pi.delivered if sf_lead.raspberry_pi else False, lead.pi_delivered, ),
            (sf_lead.facebook_account_status, lead.facebook_account_status, ),
            (sf_lead.google_account_status, lead.google_account_status, ),
            (sf_lead.raspberry_pi.tested if sf_lead.raspberry_pi else False, lead.tested, ),
            (sf_lead.fb_email, lead.fb_email, ),
            (sf_lead.fb_secret, lead.fb_secret, ),
        ):
            if new_field != old_field:
                break
        else:
            return lead

        lead.first_name = sf_lead.first_name
        lead.last_name = sf_lead.last_name
        lead.email = sf_lead.email
        lead.phone = sf_lead.phone
        lead.address = address
        lead.account_name = sf_lead.account_name
        lead.status = sf_lead.status
        lead.usps_tracking_code = sf_lead.raspberry_pi.usps_tracking_code if sf_lead.raspberry_pi else None
        lead.utm_source = sf_lead.utm_source
        lead.google_account = sf_lead.google_account
        lead.facebook_account = sf_lead.facebook_account
        lead.raspberry_pi = raspberry_pi
        lead.wrong_password = sf_lead.wrong_password
        lead.bundler_paid = sf_lead.bundler_paid
        lead.pi_delivered = sf_lead.raspberry_pi.delivered if sf_lead.raspberry_pi else False
        lead.facebook_account_status = sf_lead.facebook_account_status
        lead.google_account_status = sf_lead.google_account_status
        lead.tested = sf_lead.raspberry_pi.tested if sf_lead.raspberry_pi else False
        lead.fb_email = sf_lead.fb_email
        lead.fb_secret = sf_lead.fb_secret
        lead.save()
        return lead

    @staticmethod
    def upsert_to_sf(leads):
        pass
