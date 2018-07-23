# -*- coding:utf-8 -*-

import uuid

from django.db import models

from power.models import User


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='ID')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='更新时间')


class Mem(BaseModel):
    """
    Mem model
    """
    pass


class Cpu(BaseModel):
    """
    Cpu model
    """
    pass


class Disk(BaseModel):
    """
    Disk model
    """
    pass


class NIC(BaseModel):
    """
    NIC model
    """


class Host(BaseModel):
    """
    Host model
    """
    hostname = models.CharField(max_length=64, unique=True, verbose_name='主机名')
    intranet_ipaddress = models.GenericIPAddressField(unique=True, verbose_name='内网IP')
    network_ipaddress = models.GenericIPAddressField(unique=True, blank=True, null=True, verbose_name='外网IP')
    host_type = models.CharField(max_length=32, blank=True, null=True, verbose_name='主机类型')
    macaddress = models.CharField(max_length=32, blank=True, null=True, verbose_name='Mac地址')
    sn = models.CharField(max_length=128, blank=True, null=True, verbose_name='SN号')
    manufacturer = models.CharField(max_length=64, blank=True, null=True, verbose_name='厂商')
    hostgroup = models.CharField(max_length=64, blank=True, null=True, verbose_name='主机组')

    port = models.SmallIntegerField(default=22, blank=True, null=True, verbose_name='端口')
    os_type = models.CharField(max_length=32, blank=True, null=True, verbose_name='系统类型')
    os_version = models.CharField(max_length=64, blank=True, null=True, verbose_name='系统版本')

    mem = models.ForeignKey(Mem, blank=True, null=True, verbose_name='内存')
    cpu = models.ForeignKey(Cpu, blank=True, null=True, verbose_name='CPU')
    disk = models.ForeignKey(Disk, blank=True, null=True, verbose_name='磁盘')
    nic = models.ForeignKey(NIC, blank=True, null=True, verbose_name='网卡')

    status = models.IntegerField(verbose_name='状态')
    description = models.TextField(max_length=512, blank=True, null=True, verbose_name='描述')

    class Meta:
        verbose_name = '主机'
        verbose_name_plural = verbose_name
        permissions = (
            ('list_host', ('获取主机列表')),
            ('get_host', ('获取主机信息')),
            ('add_host', ('添加主机')),
            ('change_host', ('修改主机信息')),
            ('delete_host', ('删除主机')),
        )
        default_permissions = ()

    def __str__(self):
        return self.hostname


class HostGroup(BaseModel):
    """
    HostGroup model
    """
    name = models.CharField(max_length=64, unique=True, verbose_name='主机组名')
    description = models.TextField(max_length=512, blank=True, null=True, verbose_name='描述')

    class Meta:
        verbose_name = '主机组'
        verbose_name_plural = verbose_name
        permissions = (
            ('list_hostgroup', ('获取主机组列表')),
            ('get_hostgroup', ('获取主机组信息')),
            ('add_hostgroup', ('添加主机组')),
            ('change_hostgroup', ('修改主机组信息')),
            ('delete_hostgroup', ('删除主机组')),
        )
        default_permissions = ()

    def __str__(self):
        return self.name


class IDC(BaseModel):
    """
    IDC model
    """
    name = models.CharField(max_length=64, verbose_name='机房名')
    address = models.CharField(max_length=128, verbose_name='所在地址')
    phone = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系电话')
    manage_user = models.ForeignKey(User, related_name='idc_manager', verbose_name='联系人')

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = verbose_name
        permissions = (
            ('list_idc', ('获取机房')),
            ('get_idc', ('获取机房')),
            ('add_idc', ('添加机房')),
            ('change_idc', ('修改机房')),
            ('delete_idc', ('删除机房')),
        )
        default_permissions = ()

    def __str__(self):
        return self.name


class Cabinet(models):
    """
    Cabinet model
    """
    pass


class Service(BaseModel):
    """
    Service model
    """
    pass