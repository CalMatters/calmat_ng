# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20160603_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='works_display_five',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Works 5 Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_four',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Works 4 Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_one',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Works 1 Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_three',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Works 3 Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_two',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Works 2 Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_five',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=500, verbose_name='Works 5 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_four',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=500, verbose_name='Works 4 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_one',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=500, verbose_name='Works 1 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_three',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=500, verbose_name='Works 3 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_two',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=500, verbose_name='Works 2 URL'),
        ),
    ]