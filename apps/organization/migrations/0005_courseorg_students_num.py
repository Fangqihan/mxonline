# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20171115_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='students_num',
            field=models.IntegerField(default=0, verbose_name='学生人数'),
        ),
    ]
