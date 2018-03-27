# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-27 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.CharField(max_length=140)),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('email', models.CharField(max_length=140)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
