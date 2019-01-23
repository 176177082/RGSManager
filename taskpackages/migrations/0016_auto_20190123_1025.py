# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-23 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpackages', '0015_auto_20190123_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskpackagechunk',
            name='describe',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f'),
        ),
        migrations.AddField(
            model_name='taskpackagechunk',
            name='regiontask_name',
            field=models.CharField(default='\u4e1c\u5357\u533a\u57df', max_length=150, verbose_name='\u4efb\u52a1\u533a\u57df'),
        ),
        migrations.AddField(
            model_name='taskpackagechunk',
            name='schedule',
            field=models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=200, verbose_name='\u8fdb\u5ea6'),
        ),
        migrations.AddField(
            model_name='taskpackagechunk',
            name='user_username',
            field=models.CharField(max_length=150, null=True, verbose_name='\u5b50\u4efb\u52a1\u5305\u5f52\u5c5e\u8005'),
        ),
        migrations.AddField(
            model_name='taskpackagechunk',
            name='version',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5b50\u4efb\u52a1\u5305\u7248\u672c\u53f7'),
        ),
    ]