# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_game', '0002_auto_20170329_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='finish_time',
            field=models.DateTimeField(),
        ),
    ]
