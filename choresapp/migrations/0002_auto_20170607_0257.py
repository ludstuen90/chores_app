# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 02:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choresapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chores',
            new_name='Chore',
        ),
        migrations.RenameModel(
            old_name='Cleans',
            new_name='Clean',
        ),
    ]