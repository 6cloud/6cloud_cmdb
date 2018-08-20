# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, DjangoModelPermissions, DjangoObjectPermissions

from system.models import User, Role


class CustomPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.username == obj

    def has_permission(self, request, view):
        user = User.objects.get(username=request.username)
        if request.method in user.get_all_permissions():
            return True
        else:
            return False


class CustomDjangoModelPermission(DjangoModelPermissions):

    def has_permission(self, request, view):
        self.perms_map['GET'] = ['%(app_label)s.get_%(model_name)s']
        super(CustomDjangoModelPermission, self).has_permission(request, view)


class CustomDjangoObjectPermission(DjangoObjectPermissions):
    pass