# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-19 05:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190519_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_time_of_task',
            field=models.TimeField(default=datetime.time(10, 38, 18, 683080), help_text='Final time', verbose_name='Final time'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='start_time_of_task',
            field=models.TimeField(default=datetime.time(10, 38, 18, 683080), help_text='Starting time', verbose_name='Starting time'),
        ),
    ]
