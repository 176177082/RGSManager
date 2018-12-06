# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 05:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskpackages', '0007_auto_20181205_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskpackageversion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taskpackageversion', to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u4e1a\u5458'),
        ),
    ]