# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_auto_20160713_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name_plural': 'Contact Us Records',
                'verbose_name': 'Contact Us Record',
            },
        ),
    ]
