# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boyfriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='Name')),
                ('email', models.EmailField(max_length=64, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=24, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Chores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chore_name', models.CharField(max_length=24)),
                ('description', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Cleans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('chore_completed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='choresapp.Chores')),
                ('cleaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='choresapp.Boyfriend')),
            ],
        ),
    ]
