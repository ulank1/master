# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-08-14 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(blank=True, null=True, upload_to=post.models.image_upload_to, verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('count', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430',
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='ForumCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0424\u043e\u0440\u0443\u043c\u0430',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0424\u043e\u0440\u0443\u043c\u0430',
            },
        ),
        migrations.CreateModel(
            name='ForumSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=200, verbose_name='\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.ForumCategory', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0424\u043e\u0440\u0443\u043c\u0430',
                'verbose_name_plural': '\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0424\u043e\u0440\u0443\u043c\u0430',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.RemoveField(
            model_name='servicemaster',
            name='category',
        ),
        migrations.AddField(
            model_name='order',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.SubCategory', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='servicemaster',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.SubCategory', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='servicemaster',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Users', verbose_name='\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AddField(
            model_name='forum',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.ForumSubCategory', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='forum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Users', verbose_name='\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
