# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_userprofile_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='connected_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gcm_register',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
