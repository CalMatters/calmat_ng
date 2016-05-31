# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160527_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='partners',
            field=models.ManyToManyField(blank=True, related_name='projects_for_partner', through='pages.ProjectSortablePartners', to='business.Partner', verbose_name=b'Partners for project'),
        ),
    ]
