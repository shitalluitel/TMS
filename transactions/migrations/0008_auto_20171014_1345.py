# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_transaction_created_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_hour',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
