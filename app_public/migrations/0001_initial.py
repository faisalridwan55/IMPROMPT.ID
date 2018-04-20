# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-20 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imprompt_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baris_atas_judul', models.CharField(max_length=140)),
                ('baris_atas_description', models.TextField()),
                ('baris_tengah_judul', models.CharField(max_length=140)),
                ('baris_tengah', models.TextField(blank=True)),
                ('baris_bawah_judul', models.CharField(max_length=140)),
                ('baris_bawah', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=140)),
                ('news_short_description', models.CharField(max_length=140)),
                ('news_description', models.TextField()),
            ],
        ),
    ]
