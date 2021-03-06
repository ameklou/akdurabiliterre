# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presta', '0003_prestataire_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='prestataire',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestataire',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestataire',
            name='validate',
            field=models.BooleanField(default=True),
        ),
    ]
