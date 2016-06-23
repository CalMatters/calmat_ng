# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20160621_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, help_text='Choices limited to users who are staff (is_staff=True).', related_name='authors_articles', to='business.Person', verbose_name='By Person'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='politics_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Person'),
        ),
    ]