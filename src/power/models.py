# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


class Role(models.Model):
    """
    Role model
    """
    name = models.CharField(max_length=64, unique=True, verbose_name='角色名')
    permission = models.ManyToManyField(Permission, related_name='role_perm', verbose_name='角色权限')


class UserGroup(models.Model):
    """
    UserGroup model
    """
    group_name = models.CharField(max_length=64, unique=True, verbose_name='组名')
    permission = models.ManyToManyField(Permission, related_name='group_perm', verbose_name='角色权限')



class User(AbstractUser):
    """
    User model
    """
    id = models.UUIDField(primary_key=True, auto_created=True, verbose_name='ID')
    username = models.CharField(max_length=64, unique=True, verbose_name='用户名')
    email = models.EmailField(max_length=64, unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=128, verbose_name='密码')
    user_group = models.ForeignKey(UserGroup, related_name='user_group', verbose_name='用户组')
    role = models.ManyToManyField(Role, related_name='user_roles', verbose_name='角色')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
