# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


class Role(models.Model):
    """
    Role model
    """
    name = models.CharField(max_length=64, unique=True, verbose_name='角色名')
    permission = models.ManyToManyField(Permission, related_name='role_perm', verbose_name='角色权限')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')


class UserGroup(models.Model):
    """
    UserGroup model
    """
    group_name = models.CharField(max_length=64, unique=True, verbose_name='组名')
    group_key = models.CharField(max_length=32, unique=True, verbose_name='KEY')
    leader = models.IntegerField(default=0, verbose_name='负责人')
    desc = models.TextField(blank=True, null=True, verbose_name='描述')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')



class User(AbstractUser):
    """
    User model
    """
    id = models.UUIDField(primary_key=True, auto_created=True, verbose_name='ID')
    username = models.CharField(max_length=64, unique=True, verbose_name='用户名')
    email = models.EmailField(max_length=64, unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=128, verbose_name='密码')
    role = models.ManyToManyField(Role, related_name='user_roles', verbose_name='角色')
    permission = models.ManyToManyField(Permission, related_name='user_perm', verbose_name='用户权限')
    usergroup = models.ManyToManyField(UserGroup, related_name='user_groups', verbose_name='所属组')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
