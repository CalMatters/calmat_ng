# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20160610_1432'),
        ('pages', '0010_auto_20160609_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relatedheadlinearticle',
            options={'ordering': ('order',), 'verbose_name': 'Related Headline Article', 'verbose_name_plural': 'Related Headline Articles - first one is large'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='politics_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Author'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='politics_quote',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='atom',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headlines',
            field=models.ManyToManyField(blank=True, related_name='home_more_headlines', through='pages.RelatedHeadlineArticle', to='pages.Article', verbose_name='More Headlines'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status'),
        ),
    ]