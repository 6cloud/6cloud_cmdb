from rest_framework import viewsets

from cmdb.source import HostSerializer
from cmdb.source.models import Host


class HostView(viewsets.ModelViewSet):
    queryset = Host.object.all()
    serializer_class = HostSerializer

    def create(self, request, *args, **kwargs):
        pass