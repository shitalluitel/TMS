# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171012_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
