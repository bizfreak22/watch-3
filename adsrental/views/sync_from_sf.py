from django.views import View
from django.http import JsonResponse

from adsrental.models import Lead
from salesforce_handler.models import Lead as SFLead


class SyncFromSFView(View):
    def get(self, request):
        sf_leads = SFLead.objects.all().simple_select_related('raspberry_pi')
        leads = Lead.objects.all().select_related('raspberry_pi')
        leads_map = {}
        for lead in leads:
            leads_map[lead.leadid] = lead

        for sf_lead in sf_leads:
            Lead.upsert_from_sf(sf_lead, leads_map.get(sf_lead.id))

        return JsonResponse({
            'result': True,
        })
