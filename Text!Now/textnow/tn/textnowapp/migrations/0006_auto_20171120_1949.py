# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textnowapp', '0005_auto_20171120_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='archive',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]