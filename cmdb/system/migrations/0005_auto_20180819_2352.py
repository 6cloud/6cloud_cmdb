# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-19 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20180817_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(blank=True, related_name='user_roles', to='system.Role', verbose_name='角色'),
        ),
    ]
