from __future__ import unicode_literals

from dateutil.relativedelta import relativedelta

from django.db import models

from adsrental.models.lead_history import LeadHistory


class LeadHistoryMonth(models.Model):
    lead = models.ForeignKey('adsrental.Lead')
    date = models.DateField(db_index=True)
    days_offline = models.IntegerField(default=0)
    days_online = models.IntegerField(default=0)
    days_wrong_password = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def aggregate(self):
        self.days_offline = 0
        self.days_online = 0
        self.days_wrong_password = 0
        lead_histories = LeadHistory.objects.filter(
            lead=self.lead,
            date__gte=self.date.replace(day=1),
            date__lt=self.date + relativedelta(months=1),
        )
        for lead_history in lead_histories:
            if lead_history.checks_online and lead_history.checks_online > lead_history.checks_offline:
                self.days_online += 1
            else:
                self.days_offline += 1
            if lead_history.checks_wrong_password:
                self.days_wrong_password += 1

        self.save()

    @classmethod
    def get_or_create(cls, lead, date):
        date_month = date.replace(day=1)
        item = cls.objects.filter(date=date_month, lead=lead).first()
        if item:
            return item

        return cls(lead=lead, date=date_month)

    def get_amount(self):
        return 25. * self.days_online / (self.days_online + self.days_offline)