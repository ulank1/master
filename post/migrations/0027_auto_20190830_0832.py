# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-08-30 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_auto_20190218_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmationorder',
            name='last',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='confirmationservice',
            name='last',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]