from django.urls import path

from adsrental.views.rpi.ec2_data import EC2DataView
from adsrental.views.rpi.pi_config import PiConfigView
from adsrental.views.rpi.connection_data import ConnectionDataView


urlpatterns = [
    path('ec2_data/<rpid>/', EC2DataView.as_view(), name='rpi_ec2_data'),
    path('config/<rpid>/', PiConfigView.as_view(), name='pi_config'),
    path('/<rpid>/connection_data/', ConnectionDataView.as_view(), name='rpi_connection_data'),
]
