# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-08-14 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20180814_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
