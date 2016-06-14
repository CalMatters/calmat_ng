# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=255, verbose_name='Photographer / creator')),
                ('image_type', models.CharField(choices=[('photo', 'photo'), ('illustration', 'illustration'), ('graphic', 'graphic')], max_length=30)),
                ('license', models.CharField(choices=[('calmatters owned', 'CALmatters owned'), ('licensed', 'Licensed'), ('creative commons', 'Creative Commons')], max_length=30)),
                ('caption', models.CharField(max_length=255)),
                ('alt_tag', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date taken')),
                ('file', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='MediaSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media_manager.MediaSource'),
        ),
    ]