# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-13 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskpackages', '0018_auto_20190213_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regiontaskchunk',
            old_name='filechunk',
            new_name='file',
        ),
    ]