# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import taskpackages.models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpackages', '0006_auto_20181205_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskpackageversion',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=taskpackages.models.user_directory_path1, verbose_name='\u4efb\u52a1\u5305\u8def\u5f84'),
        ),
    ]