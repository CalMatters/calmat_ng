# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_manager', '0004_auto_20160616_1144'),
        ('pages', '0050_auto_20160919_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposition',
            name='facebook_image',
            field=models.ForeignKey(blank=True, help_text='Image size should be 600 x 315 for best results (or 1200 x 630 for high resolution)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposition_with_facebook_image', to='media_manager.MediaItem'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='featured_image_credit',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Credit'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='featured_image_description',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Description'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='featured_image_title_position',
            field=models.CharField(choices=[('topleft', 'Top-Left'), ('topright', 'Top-Right'), ('bottomleft', 'Bottom-Left'), ('bottomright', 'Bottom-Right')], default='topleft', max_length=30, verbose_name='Position'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='featured_image_title_shade',
            field=models.CharField(choices=[('dark', 'Dark'), ('light', 'Light')], default='dark', max_length=30, verbose_name='Shade'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='headline_layout',
            field=models.CharField(choices=[('below', 'Below Image'), ('below_big', 'Below Image - Big'), ('over', 'Over Image'), ('above', 'Above Image')], default='below', max_length=30, verbose_name='Headline Layout'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='icon_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='props_icon_image', to='media_manager.MediaItem', verbose_name='Icon Image'),
        ),
        migrations.AlterField(
            model_name='proposition',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='props_with_image', to='media_manager.MediaItem', verbose_name='Featured Image'),
        ),
    ]