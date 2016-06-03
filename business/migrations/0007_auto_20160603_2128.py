# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20160601_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.CharField(blank=True, help_text='Will be auto-generated from the title.', max_length=2000, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='slug',
            field=models.CharField(blank=True, help_text='Will be auto-generated from the title.', max_length=2000, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='partnerowner',
            name='slug',
            field=models.CharField(blank=True, help_text='Will be auto-generated from the title.', max_length=2000, null=True, verbose_name='URL'),
        ),
    ]
