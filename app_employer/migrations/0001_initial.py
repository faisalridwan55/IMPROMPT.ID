# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-30 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_creator_profile_id', models.CharField(max_length=140)),
                ('country', models.CharField(max_length=140)),
                ('province', models.CharField(max_length=140)),
                ('city', models.CharField(max_length=140)),
                ('company_name', models.CharField(max_length=140)),
                ('company_description', models.TextField()),
                ('company_website', models.CharField(max_length=140)),
                ('company_logo', models.FileField(upload_to='company_logo/')),
            ],
        ),
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
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity_category', models.CharField(max_length=140)),
                ('opportunity_field', models.CharField(max_length=140)),
                ('durations', models.CharField(max_length=140)),
                ('salary', models.CharField(max_length=140)),
                ('participants_needed', models.CharField(max_length=140)),
                ('requirements', models.TextField()),
                ('description', models.TextField()),
                ('contact_person_phone_number', models.CharField(max_length=140)),
                ('opportunity_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employer.Company')),
            ],
        ),
    ]
