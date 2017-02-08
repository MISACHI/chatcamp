# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-04 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('contacts', models.TextField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('skills', models.CharField(max_length=500)),
                ('profession', models.TextField(max_length=100)),
                ('brief_description', models.CharField(max_length=500)),
                ('app_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Registration')),
            ],
        ),
    ]