# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_userprofile_base'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Base',
        ),
    ]