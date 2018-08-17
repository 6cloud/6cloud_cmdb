# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import authenticate
from rest_framework import authtoken
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from system.serializers import UserSerializer, RoleSerializer
from system.models import User, Role


class UserLoginApi(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request['POST']
        username = data.get('username')
        password = data.get('password')
        authenticater = authenticate(username=username, password=password)
        if authenticater:
            pass
            return Response(authenticater, status=HTTP_200_OK)
        return Response({'msg': '认证失败!'}, status=HTTP_400_BAD_REQUEST)



class UserActionApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()

    # def list(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass


class RoleActionApi(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = ()
    authentication_classes = ()
