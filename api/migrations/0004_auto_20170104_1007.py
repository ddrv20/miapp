# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170103_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
