# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-01 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190301_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='dateplanted',
            field=models.DateField(),
        ),
    ]
