# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0003_auto_20160728_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='jobpage',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobpage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
