# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, DjangoModelPermissions, DjangoObjectPermissions,SAFE_METHODS

from system.models import User, Role


class CommonPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.username == obj

    def has_permission(self, request, view):
        user = User.objects.get(username=request.username)
        if request.method in user.get_all_permissions():
            return True
        else:
            return False






