# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0058_auto_20160919_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='headline_layout',
            field=models.CharField(choices=[('below', 'Below Image'), ('below_big', 'Below Image - Big'), ('over', 'Over Image'), ('above', 'Above Image')], default='below', max_length=30, verbose_name='Headline Layout'),
        ),
        migrations.AlterField(
            model_name='proposition',
            name='headline_layout',
            field=models.CharField(choices=[('below', 'Below Image'), ('below_big', 'Below Image - Big'), ('over', 'Over Image'), ('above', 'Above Image')], default='below', max_length=30, verbose_name='Headline Layout'),
        ),
        migrations.AlterField(
            model_name='voterguide',
            name='headline_layout',
            field=models.CharField(choices=[('below', 'Below Image'), ('below_big', 'Below Image - Big'), ('over', 'Over Image'), ('above', 'Above Image')], default='below', max_length=30, verbose_name='Headline Layout'),
        ),
    ]
