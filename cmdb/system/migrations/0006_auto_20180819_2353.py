# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-19 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20180819_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(blank=True, related_name='role_perm', to='auth.Permission', verbose_name='角色权限'),
        ),
    ]
