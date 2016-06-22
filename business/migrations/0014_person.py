# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 23:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media_manager', '0004_auto_20160616_1144'),
        ('business', '0013_auto_20160620_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('description', models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)')),
                ('slug', models.CharField(blank=True, help_text='Will be auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('job_title', models.CharField(blank=True, default='', max_length=100)),
                ('twitter', models.CharField(blank=True, default='', help_text='Adding a Facebook url will enable Facebook authoring.  i.e. https://www.facebook.com/your_name', max_length=256, verbose_name='Twitter @')),
                ('facebook_url', models.CharField(blank=True, default='', help_text='Adding a Facebook url will enable Facebook authoring.  i.e. https://www.facebook.com/your_name', max_length=256, verbose_name='Facebook URL')),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='media_manager.MediaItem')),
                ('user', models.OneToOneField(help_text='Connects the `author` object to a `User`to pull in the profile photo on a post.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Author',
            },
        ),
    ]
