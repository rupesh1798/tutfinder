# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-06 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackcourse',
            name='detail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]