# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20171111_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='visit_number',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
