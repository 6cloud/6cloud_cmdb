# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-17 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='idc',
            name='manage_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idc_manager', to=settings.AUTH_USER_MODEL, verbose_name='联系人'),
        ),
        migrations.AddField(
            model_name='host',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_application', to='source.Application', verbose_name='所属应用'),
        ),
        migrations.AddField(
            model_name='host',
            name='colony',
            field=models.ManyToManyField(related_name='host_colony', to='source.Colony', verbose_name='所属集群'),
        ),
        migrations.AddField(
            model_name='host',
            name='cpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.Cpu', verbose_name='CPU'),
        ),
        migrations.AddField(
            model_name='host',
            name='disk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.Disk', verbose_name='磁盘'),
        ),
        migrations.AddField(
            model_name='host',
            name='mem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.Mem', verbose_name='内存'),
        ),
        migrations.AddField(
            model_name='host',
            name='nic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.NIC', verbose_name='网卡'),
        ),
        migrations.AddField(
            model_name='host',
            name='systemuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_systemuser', to='source.SystemUser', verbose_name='系统用户'),
        ),
        migrations.AddField(
            model_name='colony',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colony_application', to='source.Application', verbose_name='所属应用'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='hosts',
            field=models.ManyToManyField(related_name='cabinet_hosts', to='source.Host', verbose_name='主机'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinet_idc', to='source.IDC', verbose_name='所属机房'),
        ),
        migrations.AddField(
            model_name='business',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='application',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_business', to='source.Business', verbose_name='所属业务'),
        ),
        migrations.AddField(
            model_name='application',
            name='cs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_cs', to=settings.AUTH_USER_MODEL, verbose_name='安全负责人'),
        ),
        migrations.AddField(
            model_name='application',
            name='dev',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_dev', to=settings.AUTH_USER_MODEL, verbose_name='研发负责人'),
        ),
        migrations.AddField(
            model_name='application',
            name='ops',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_ops', to=settings.AUTH_USER_MODEL, verbose_name='运维负责人'),
        ),
        migrations.AddField(
            model_name='application',
            name='qa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_qa', to=settings.AUTH_USER_MODEL, verbose_name='测试负责人'),
        ),
    ]
