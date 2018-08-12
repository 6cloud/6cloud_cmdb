from rest_framework import viewsets

from source.serializers import HostSerializer
from source.models import Host


class HostView(viewsets.ModelViewSet):
    queryset = Host.object.all()
    serializer_class = HostSerializer

    def create(self, request, *args, **kwargs):
        pass