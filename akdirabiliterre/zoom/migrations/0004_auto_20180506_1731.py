# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zoom', '0003_auto_20180506_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoom',
            name='project_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]