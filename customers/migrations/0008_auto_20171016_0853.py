# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20171016_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]