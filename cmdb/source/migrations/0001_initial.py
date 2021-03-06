# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-17 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='应用')),
            ],
            options={
                'verbose_name_plural': '业务',
                'verbose_name': '业务',
                'permissions': (('list_application', '获取应用列表'), ('get_application', '获取应用信息'), ('add_application', '添加应用'), ('change_application', '修改应用信息'), ('delete_application', '删除应用')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='业务名')),
            ],
            options={
                'verbose_name_plural': '业务',
                'verbose_name': '业务',
                'permissions': (('list_business', '获取业务列表'), ('get_business', '获取业务信息'), ('add_business', '添加业务'), ('change_business', '修改业务信息'), ('delete_business', '删除业务')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('address', models.CharField(max_length=128, unique=True, verbose_name='所在机房位置')),
                ('unum', models.IntegerField(default=0, verbose_name='机柜U个数')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
            ],
            options={
                'verbose_name_plural': '机柜',
                'verbose_name': '机柜',
                'permissions': (('list_cabinet', '获取机柜列表'), ('get_cabinet', '获取机柜信息'), ('add_cabinet', '添加机柜'), ('change_cabinet', '修改机柜信息'), ('delete_cabinet', '删除机柜')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='集群名')),
            ],
            options={
                'verbose_name_plural': '主机组',
                'verbose_name': '主机组',
                'permissions': (('list_hostgroup', '获取主机组列表'), ('get_hostgroup', '获取主机组信息'), ('add_hostgroup', '添加主机组'), ('change_hostgroup', '修改主机组信息'), ('delete_hostgroup', '删除主机组')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='主机名')),
                ('intranet_ipaddress', models.GenericIPAddressField(unique=True, verbose_name='内网IP')),
                ('network_ipaddress', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='外网IP')),
                ('host_type', models.CharField(default='server', max_length=32, verbose_name='主机类型')),
                ('macaddress', models.CharField(blank=True, max_length=32, null=True, verbose_name='Mac地址')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN号')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='厂商')),
                ('port', models.SmallIntegerField(default=22, verbose_name='端口')),
                ('os_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='系统类型')),
                ('os_version', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统版本')),
                ('status', models.IntegerField(choices=[(1, '使用中'), (2, '空闲中'), (3, '故障中'), (4, '测试机'), (5, '开发机'), (6, '维修中')], default=1, verbose_name='状态')),
                ('description', models.TextField(blank=True, max_length=512, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': '主机',
                'verbose_name': '主机',
                'permissions': (('list_host', '获取主机列表'), ('get_host', '获取主机信息'), ('add_host', '添加主机'), ('change_host', '修改主机信息'), ('delete_host', '删除主机')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=64, verbose_name='机房名')),
                ('address', models.CharField(max_length=128, verbose_name='所在地址')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='联系电话')),
            ],
            options={
                'verbose_name_plural': '机房',
                'verbose_name': '机房',
                'permissions': (('list_idc', '获取机房列表'), ('get_idc', '获取机房信息'), ('add_idc', '添加机房'), ('change_idc', '修改机房信息'), ('delete_idc', '删除机房')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Mem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(blank=True, max_length=256, null=True, verbose_name='密码')),
                ('private_key', models.TextField(blank=True, max_length=4096, null=True, verbose_name='私钥')),
                ('public_key', models.TextField(blank=True, max_length=4096, null=True, verbose_name='公钥')),
            ],
            options={
                'verbose_name_plural': '系统用户',
                'verbose_name': '系统用户',
                'permissions': (('list_systemuser', '获取系统用户列表'), ('get_systemuser', '获取系统用户信息'), ('add_systemuser', '添加系统用户'), ('change_systemuser', '修改系统用户信息'), ('delete_systemuser', '删除系统用户')),
                'default_permissions': (),
            },
        ),
    ]
