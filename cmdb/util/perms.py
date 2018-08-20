# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, DjangoModelPermissions, DjangoObjectPermissions

from system.models import User, Role


class CommonPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        pass

    def has_permission(self, request, view):
        pass






