# -*- coding: utf-8 -*-

from rest_framework import serializers

from system.models import User, Role


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'permission', 'create_time', 'update_time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_roles = RoleSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_roles', 'is_active', 'is_superuser')