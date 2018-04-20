# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-20 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.CharField(max_length=140)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('email', models.CharField(max_length=140)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('birthday', models.DateTimeField(blank=True)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='application_form',
            name='job_seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_job_seeker.Job_Seeker'),
        ),
        migrations.AddField(
            model_name='application_form',
            name='opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employer.Opportunity'),
        ),
    ]
