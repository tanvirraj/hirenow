# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20160204_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='base',
        ),
    ]