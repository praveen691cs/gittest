# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20180626_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
