# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_courseorg_has_favor'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='has_favor',
            field=models.BooleanField(default=False, max_length=10, verbose_name='会否收藏'),
        ),
    ]
