# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 14:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('building_name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1)),
                ('upgrade_scheduled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100)),
                ('resources', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('timer_id', models.AutoField(primary_key=True, serialize=False)),
                ('finish_time', models.TimeField()),
                ('action', models.CharField(choices=[('building_up', 'upgrade')], max_length=5)),
                ('args', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['finish_time'],
            },
        ),
        migrations.AddField(
            model_name='building',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_game.City'),
        ),
    ]
