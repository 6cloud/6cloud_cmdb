# -*- coding:utf-8 -*-

from rest_framework import serializers

from source.models import Host


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('intranet_ipaddress', 'hostname', 'port')