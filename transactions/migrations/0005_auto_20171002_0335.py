# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20171001_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
