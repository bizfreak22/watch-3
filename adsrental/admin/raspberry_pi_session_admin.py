from __future__ import unicode_literals

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils import timezone

from adsrental.models.raspberry_pi_session import RaspberryPiSession


class RaspberryPiSessionAdmin(admin.ModelAdmin):
    model = RaspberryPiSession
    list_display = (
        'id',
        'raspberry_pi_link',
        'start_date',
        'end_date',
        'duration',
    )
    list_select_related = ('raspberry_pi', )
    search_fields = ('raspberry_pi__rpid', )
    raw_id_fields = ('raspberry_pi', )

    def raspberry_pi_link(self, obj):
        result = []
        if obj.raspberry_pi:
            result.append('<a target="_blank" href="{url}?q={rpid}">{rpid}</a> (<a target="_blank" href="/log/{rpid}">Logs</a>, <a href="{rdp_url}">RDP</a>, <a href="{config_url}">Config file</a>)'.format(
                rdp_url=reverse('rdp', kwargs={'rpid': obj.raspberry_pi}),
                url=reverse('admin:adsrental_raspberrypi_changelist'),
                config_url=reverse('farming_pi_config', kwargs={'rpid': obj.raspberry_pi}),
                rpid=obj.raspberry_pi,
            ))

        return '\n'.join(result)

    def duration(self, obj):
        end_date = obj.end_date or timezone.now()
        delta = end_date - obj.start_date
        if delta.seconds < 5:
            return 'now'
        days = delta.days
        delta_seconds = delta.seconds % (60 * 60 * 24)
        return '{days}{hh}:{mm}:{ss}'.format(
            days='{} days and '.format(days) if days else '',
            hh='%02d' % (delta_seconds // 60 // 60),
            mm='%02d' % (delta_seconds // 60 % 60),
            ss='%02d' % (delta_seconds % 60),
        )

    raspberry_pi_link.short_description = 'Raspberry Pi'
    raspberry_pi_link.allow_tags = True
