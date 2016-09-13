# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-13 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposition',
            name='publish_date',
            field=models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='proposition',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='props_with_image', to='media_manager.MediaItem', verbose_name='Icon Image'),
        ),
    ]
