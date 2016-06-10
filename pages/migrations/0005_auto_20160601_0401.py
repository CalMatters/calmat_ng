# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 04:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20160527_2321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relatedarticle',
            options={'ordering': ('order',), 'verbose_name': 'Related Article', 'verbose_name_plural': 'Related Articles'},
        ),
        migrations.AddField(
            model_name='relatedarticle',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, help_text='Choices limited to users who are staff (is_staff=True).', related_name='authors_articles', to='business.Author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='article',
            name='custom_post_type',
            field=models.CharField(choices=[('articles', 'Articles'), ('expertperspectives', 'Expert Perspectives'), ('external', 'External Link'), ('press', 'Press Release'), ('readerreactions', 'Reader Reactions'), ('updates', 'Updates')], default='articles', max_length=30, verbose_name='Content Type'),
        ),
        migrations.AlterField(
            model_name='article',
            name='custom_source',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='External Source'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='facebook_share_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Image size should be 600 x 315 for best results (or 1200 x 630 for high resolution)', null=True, upload_to='posts/', verbose_name='Facebook Share Image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='posts/', verbose_name='Featured Image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image_credit',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Credit'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image_description',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image_title_position',
            field=models.CharField(choices=[('topleft', 'Top-Left'), ('topright', 'Top-Right'), ('bottomleft', 'Bottom-Left'), ('bottomright', 'Bottom-Right')], default='topleft', max_length=30, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image_title_shade',
            field=models.CharField(choices=[('dark', 'Dark'), ('light', 'Light')], default='dark', max_length=30, verbose_name='Shade'),
        ),
        migrations.AlterField(
            model_name='article',
            name='guest_author',
            field=models.CharField(blank=True, default='', help_text='*Guest Author* will be prepend regular Authors selected above.', max_length=100, verbose_name='Guest Author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='headline_layout',
            field=models.CharField(choices=[('below', 'Below Image'), ('below_big', 'Below Image - Big'), ('over', 'Over Image'), ('above', 'Above Image')], default='below', max_length=30, verbose_name='Headline Layout'),
        ),
        migrations.AlterField(
            model_name='article',
            name='layout',
            field=models.CharField(choices=[('sidebar', 'Sidebar'), ('singlecolumn', 'Single Column')], default='sidebar', max_length=30, verbose_name='Layout'),
        ),
        migrations.AlterField(
            model_name='article',
            name='news_analysis',
            field=models.BooleanField(default=False, help_text='Check this box if this article should display in the POLITICS Menu', verbose_name='Politics'),
        ),
        migrations.AlterField(
            model_name='article',
            name='social_title',
            field=models.CharField(blank=True, default='', help_text='Title used when submitting article to social sites.', max_length=200, verbose_name='Social Sharing Title'),
        ),
        migrations.AlterField(
            model_name='atom',
            name='default_display_type',
            field=models.CharField(choices=[('image', 'Image Only'), ('text', 'Headline and Text')], default='text', help_text='When inserted into articles, atoms will appear as either the featured image,or the headline and content. This can be overridden in the parent article.', max_length=10),
        ),
        migrations.AlterField(
            model_name='atom',
            name='description',
            field=models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)'),
        ),
        migrations.AlterField(
            model_name='atom',
            name='featured_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='atoms/', verbose_name='Featured Image'),
        ),
        migrations.AlterField(
            model_name='atom',
            name='headline',
            field=models.CharField(blank=True, help_text='The displayed headline for this atom when viewed as a piece of content.', max_length=200),
        ),
        migrations.AlterField(
            model_name='atom',
            name='modal_layout',
            field=models.CharField(choices=[('featured_left', 'Featured Image Left'), ('content_left', 'Content Left'), ('content_html_left', 'Content + HTML Left'), ('html_left', 'HTML Left')], default='featured_left', help_text='Choose what to show in the left side of a atom modal window.', max_length=20),
        ),
        migrations.AlterField(
            model_name='atom',
            name='modal_layout_right',
            field=models.CharField(choices=[('desc_right', 'Description Right'), ('content_right', 'Content Right'), ('empty_right', 'Empty Right')], default='desc_right', help_text='Choose what to show in the right side of a atom modal window.', max_length=20),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='masthead_copy',
            field=models.CharField(default='A nonprofit, nonpartisan media venture producing compelling stories on policies, personalities and money in Sacramento.', help_text='Text displayed in top black bar for the homepage.', max_length=125),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='primary_article',
            field=models.ForeignKey(help_text='Article displayed front and center, largest', on_delete=django.db.models.deletion.CASCADE, related_name='primary_on_homepages', to='pages.Article', verbose_name='Primary Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='secondary_article_left',
            field=models.ForeignKey(help_text='Article displayed below primary article to the left', on_delete=django.db.models.deletion.CASCADE, related_name='secondary_left_on_homepages', to='pages.Article', verbose_name='Left Secondary Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='secondary_article_right',
            field=models.ForeignKey(help_text='Article displayed below primary article to the right', on_delete=django.db.models.deletion.CASCADE, related_name='secondary_right_on_homepages', to='pages.Article', verbose_name='Right Secondary Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='the_basics_four',
            field=models.ForeignKey(help_text='Four Article in the The Basics', on_delete=django.db.models.deletion.CASCADE, related_name='basics_four_on_homepages', to='pages.Article', verbose_name='Bottom Article in The Basics'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='the_basics_one',
            field=models.ForeignKey(help_text='First Article in the The Basics', on_delete=django.db.models.deletion.CASCADE, related_name='basics_one_on_homepages', to='pages.Article', verbose_name='Top Article in The Basics'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='the_basics_three',
            field=models.ForeignKey(help_text='Third Article in the The Basics', on_delete=django.db.models.deletion.CASCADE, related_name='basics_three_on_homepages', to='pages.Article', verbose_name='Third Article in The Basics'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='the_basics_two',
            field=models.ForeignKey(help_text='Second Article in the The Basics', on_delete=django.db.models.deletion.CASCADE, related_name='basics_two_on_homepages', to='pages.Article', verbose_name='Second Article in The Basics'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_five',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_four',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_one',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_three',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_display_two',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_five',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=20, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_four',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=20, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_one',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=20, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_three',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=20, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='works_url_two',
            field=models.CharField(blank=True, default='', help_text='A valid http:// or https:// link', max_length=20, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='onramp',
            name='custom_link',
            field=models.CharField(blank=True, default='', max_length=1200, verbose_name='More Link'),
        ),
        migrations.AlterField(
            model_name='onramp',
            name='description',
            field=models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='atom',
            field=models.ForeignKey(blank=True, help_text='Appears on the right.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_showing_atom', to='pages.Atom', verbose_name='Project Atom'),
        ),
        migrations.AlterField(
            model_name='project',
            name='atom_layout',
            field=models.CharField(choices=[('image-headline', 'Image + Headline'), ('image', 'Featured Image Only'), ('atom-block', 'Atom Block'), ('embedded', 'Embeded Content <iframe>')], default='image-headline', help_text='Atom layout', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='projects', to='categories.Category', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='expert_perspectives_articles',
            field=models.ManyToManyField(blank=True, related_name='projects_showing_article_as_expert_perspective', through='pages.ProjectSortableExpertPerspectivesArticle', to='pages.Article', verbose_name='Expert Perspectives Articles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='project_images/', verbose_name='Featured Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='projects_showing_article_as_feature', through='pages.ProjectSortableFeaturedArticle', to='pages.Article', verbose_name='Featured Articles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='onramp',
            field=models.ForeignKey(blank=True, help_text='Appears on the left.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_showing_onramp', to='pages.OnRamp', verbose_name='Project OnRamp'),
        ),
        migrations.AlterField(
            model_name='project',
            name='partners',
            field=models.ManyToManyField(blank=True, related_name='projects_for_partner', through='pages.ProjectSortablePartners', to='business.Partner', verbose_name='Partners for project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='quotes',
            field=models.ManyToManyField(blank=True, related_name='projects_showing_quote', through='pages.ProjectSortableQuotes', to='pages.Quote', verbose_name='Quotes'),
        ),
        migrations.AlterField(
            model_name='project',
            name='reader_reactions_articles',
            field=models.ManyToManyField(blank=True, related_name='projects_show_article_as_reader_reaction', through='pages.ProjectSortableReaderReactionsArticle', to='pages.Article', verbose_name='Reader Reactions Articles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='related_articles',
            field=models.ManyToManyField(blank=True, related_name='projects_showing_article_as_related', through='pages.ProjectSortableRelatedArticle', to='pages.Article', verbose_name='Related Articles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='storify_embed',
            field=models.TextField(blank=True, default='', verbose_name='Storify Embed'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updates_articles',
            field=models.ManyToManyField(blank=True, related_name='projects_showing_article_as_update', through='pages.ProjectSortableUpdatesArticles', to='pages.Article', verbose_name='Updates Articles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='visualizations',
            field=models.ManyToManyField(blank=True, related_name='visualizations', through='pages.ProjectSortableVisualizations', to='pages.Atom', verbose_name='Visualizations'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='attribution',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Attribution'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='custom_link',
            field=models.CharField(blank=True, default='', max_length=1200, verbose_name='More Link'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='description',
            field=models.TextField(blank=True, default='', max_length=135, verbose_name='Description (135 Chars)'),
        ),
    ]
