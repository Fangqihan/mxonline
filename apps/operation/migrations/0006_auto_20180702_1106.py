# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-02 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20180601_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userask',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='联系电话'),
        ),
    ]