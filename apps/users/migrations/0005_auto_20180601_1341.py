# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-01 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171115_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelTable(
            name='banner',
            table='轮播图',
        ),
        migrations.AlterModelTable(
            name='emailverifyrecord',
            table='邮箱验证码',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='用户信息',
        ),
    ]
