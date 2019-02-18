# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-01-16 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20181123_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_owner', models.IntegerField(blank=True, null=True)),
                ('type_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LikeOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_owner', models.IntegerField(blank=True, null=True)),
                ('type_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LikeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_owner', models.IntegerField(blank=True, null=True)),
                ('type_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='commentuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='forum',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AddField(
            model_name='forum',
            name='lat',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='lng',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id_owner',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CommentUser',
        ),
    ]