# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-13 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import taskpackages.models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpackages', '0016_auto_20190123_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionTaskChunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='\u4efb\u52a1\u533a\u57df')),
                ('filechunk', models.FileField(null=True, upload_to=taskpackages.models.file_chunk_path, verbose_name='\u6587\u4ef6\u5207\u7247')),
                ('chunk', models.IntegerField(null=True, verbose_name='\u7b2c\u51e0\u4e2a')),
                ('chunks', models.IntegerField(null=True, verbose_name='\u5171\u7b2c\u51e0\u4e2a')),
                ('file_md5', models.CharField(max_length=128, null=True, verbose_name='MD5')),
                ('chunk_md5', models.CharField(max_length=128, null=True, verbose_name='\u6587\u4ef6\u5207\u5757md5')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('status', models.CharField(default='\u5904\u7406\u4e2d', max_length=200, verbose_name='\u72b6\u6001')),
                ('mapindexsde', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868sde')),
                ('rgssde', models.CharField(max_length=1000, null=True, verbose_name='rgssde')),
                ('basemapservice', models.CharField(max_length=1000, null=True, verbose_name='\u5e95\u56fe\u670d\u52a1')),
                ('mapindexfeatureservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u8981\u7d20\u670d\u52a1')),
                ('mapindexmapservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u5730\u56fe\u670d\u52a1')),
                ('mapindexschedulemapservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u8fdb\u5ea6\u670d\u52a1')),
                ('describe', models.CharField(max_length=2000, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u6587\u4ef6\u5207\u7247',
                'verbose_name_plural': '\u6587\u4ef6\u5207\u7247',
            },
        ),
        migrations.CreateModel(
            name='RegionTaskMerge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '\u4efb\u52a1\u533a\u57df\u5df2\u5b58\u5728'}, max_length=200, null=True, unique=True, verbose_name='\u4efb\u52a1\u533a\u57df')),
                ('status', models.CharField(default='\u5904\u7406\u4e2d', max_length=200, verbose_name='\u72b6\u6001')),
                ('mapindexsde', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868sde')),
                ('rgssde', models.CharField(max_length=1000, null=True, verbose_name='rgssde')),
                ('basemapservice', models.CharField(max_length=1000, null=True, verbose_name='\u5e95\u56fe\u670d\u52a1')),
                ('mapindexfeatureservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u8981\u7d20\u670d\u52a1')),
                ('mapindexmapservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u5730\u56fe\u670d\u52a1')),
                ('mapindexschedulemapservice', models.CharField(max_length=1000, null=True, verbose_name='\u63a5\u56fe\u8868\u8fdb\u5ea6\u670d\u52a1')),
                ('describe', models.CharField(max_length=2000, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('file', models.FileField(blank=True, null=True, upload_to=taskpackages.models.file_chunk_path, verbose_name='\u4efb\u52a1\u5305\u6587\u4ef6')),
                ('md5', models.CharField(max_length=32, null=True, verbose_name='\u6587\u4ef6MD5')),
            ],
            options={
                'verbose_name': '\u5b50\u4efb\u52a1\u5305\u5408\u5e76',
                'verbose_name_plural': '\u5b50\u4efb\u52a1\u5305\u5408\u5e76',
            },
        ),
        migrations.DeleteModel(
            name='TaskPackageChunk',
        ),
        migrations.DeleteModel(
            name='TaskPackageSonMerge',
        ),
        migrations.AddField(
            model_name='regiontask',
            name='md5',
            field=models.CharField(max_length=32, null=True, verbose_name='\u6587\u4ef6MD5'),
        ),
    ]