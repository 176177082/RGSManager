# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-07 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpackages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EchartSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskpackage_schedule', models.CharField(max_length=150, null=True, unique=True, verbose_name='\u4efb\u52a1\u5305\u5904\u7406\u8fdb\u5ea6')),
                ('count', models.IntegerField(default=0, null=True, verbose_name='\u4efb\u52a1\u5305\u6570\u91cf')),
            ],
        ),
        migrations.CreateModel(
            name='EchartTaskPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_reallyname', models.CharField(max_length=150, null=True, unique=True, verbose_name='\u4f5c\u4e1a\u5458')),
                ('count', models.IntegerField(default=0, null=True, verbose_name='\u4efb\u52a1\u5305\u6570\u91cf')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=32, verbose_name='\u4efb\u52a1\u5305\u8fdb\u5ea6')),
            ],
            options={
                'verbose_name': '\u8fdb\u5ea6\u8868',
                'verbose_name_plural': '\u8fdb\u5ea6\u8868',
            },
        ),
        migrations.AddField(
            model_name='taskpackage',
            name='mapnumcounts',
            field=models.IntegerField(default=0, null=True, verbose_name='\u56fe\u5e45\u6570'),
        ),
        migrations.AddField(
            model_name='taskpackage',
            name='newtaskpackagesonfornotice',
            field=models.IntegerField(default=0, null=True, verbose_name='\u6d88\u606f\u63d0\u9192'),
        ),
        migrations.AddField(
            model_name='taskpackage',
            name='reallyname',
            field=models.CharField(default=None, max_length=150, null=True, verbose_name='\u4f5c\u4e1a\u5458\u771f\u5b9e\u59d3\u540d'),
        ),
        migrations.AddField(
            model_name='taskpackage',
            name='schedule',
            field=models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=32, verbose_name='\u4efb\u52a1\u5305\u8fdb\u5ea6'),
        ),
        migrations.AddField(
            model_name='taskpackageson',
            name='schedule',
            field=models.CharField(default='\u672a\u6307\u5b9a\u72b6\u6001', max_length=32, verbose_name='\u4efb\u52a1\u5305\u8fdb\u5ea6'),
        ),
        migrations.AlterField(
            model_name='taskpackage',
            name='describe',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='taskpackage',
            name='mapnums',
            field=models.CharField(max_length=65536, null=True, verbose_name='\u56fe\u53f7\u96c6'),
        ),
        migrations.AlterField(
            model_name='taskpackage',
            name='name',
            field=models.CharField(error_messages={'unique': '\u4efb\u52a1\u5305\u540d\u79f0\u5df2\u5b58\u5728'}, max_length=150, unique=True, verbose_name='\u4efb\u52a1\u5305\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='taskpackageson',
            name='describe',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f'),
        ),
    ]