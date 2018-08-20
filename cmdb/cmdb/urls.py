"""cloud_cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='6Cloud_cmdb API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

from system.views import UserActionApi, RoleActionApi

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', UserActionApi)
router.register('role', RoleActionApi)


urlpatterns = [
    url(r'^swagger/', schema_view, name='swagger'),
    # url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]
