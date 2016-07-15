# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='name',
            field=models.CharField(default='Donate Page 1', help_text='Used for internal tracking only.', max_length=50),
            preserve_default=False,
        ),
    ]
