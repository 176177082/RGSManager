# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-14 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import taskpackages.models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpackages', '0003_auto_20190107_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '\u4efb\u52a1\u5305\u533a\u57df\u540d\u79f0\u5df2\u5b58\u5728'}, max_length=200, null=True, unique=True, verbose_name='\u4efb\u52a1\u533a\u57df')),
                ('file', models.FileField(blank=True, null=True, upload_to=taskpackages.models.user_directory_path, verbose_name='\u4efb\u52a1\u5305\u6587\u4ef6')),
                ('basemapservice', models.CharField(max_length=1000, null=True, verbose_name='\u5e95\u56fe\u670d\u52a1')),
                ('mapindexfeatureservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u8981\u7d20\u670d\u52a1')),
                ('mapindexmapservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u5730\u56fe\u670d\u52a1')),
                ('mapindexschedulemapservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u8fdb\u5ea6\u670d\u52a1')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u5305\u533a\u57df',
                'verbose_name_plural': '\u4efb\u52a1\u5305\u533a\u57df',
            },
        ),
        migrations.CreateModel(
            name='TaskPackageScheduleSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=200, verbose_name='\u4efb\u52a1\u5305\u8fdb\u5ea6')),
            ],
            options={
                'verbose_name': '\u8fdb\u5ea6\u8868',
                'verbose_name_plural': '\u8fdb\u5ea6\u8868',
            },
        ),
        migrations.AlterField(
            model_name='taskpackage',
            name='schedule',
            field=models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=200, verbose_name='\u4efb\u52a1\u5305\u8fdb\u5ea6'),
        ),
        migrations.AlterField(
            model_name='taskpackageson',
            name='schedule',
            field=models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=200, verbose_name='\u4efb\u52a1\u5305\u8fdb\u5ea6'),
        ),
    ]
