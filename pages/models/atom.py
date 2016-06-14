from django.utils.translation import ugettext_lazy as _
from django.db import models

from versatileimagefield.fields import VersatileImageField

from categories.models import Category
from sites.models import Named, Publishable, TimeStamped, ContentContainer

ATOM_DEFAULT_DISPLAY_TYPE_CHOICES = (
    ('image', 'Image Only'),
    ('text', 'Headline and Text'),
)

ATOM_MODAL_LAYOUT = (
    ('featured_left', 'Featured Image Left'),
    ('content_left', 'Content Left'),
    ('content_html_left', 'Content + HTML Left'),
    ('html_left', 'HTML Left'),
)

ATOM_MODAL_LAYOUT_RIGHT = (
    ('desc_right', 'Description Right'),
    ('content_right', 'Content Right'),
    ('empty_right', 'Empty Right'),
)


class Atom(Named, Publishable, ContentContainer, TimeStamped):

    headline = models.CharField(
        max_length=200,
        blank=True,
        help_text='The displayed headline for this atom '
                  'when viewed as a piece of content.')

    default_display_type = models.CharField(
        max_length=10,
        choices=ATOM_DEFAULT_DISPLAY_TYPE_CHOICES,
        default='text',
        help_text='When inserted into articles, atoms will '
                  'appear as either the featured image,'
                  'or the headline and content. '
                  'This can be overridden in the parent article.')

    featured_image = VersatileImageField(
        verbose_name=_("Featured Image"),
        upload_to='atoms/',
        null=True,
        blank=True)

    categories = models.ManyToManyField(
        Category,
        verbose_name=_("Categories"),
        blank=True,
        related_name="atoms")

    modal_layout = models.CharField(
        max_length=20,
        choices=ATOM_MODAL_LAYOUT,
        default='featured_left',
        help_text='Choose what to show in the '
                  'left side of a atom modal window.')

    modal_layout_right = models.CharField(
        max_length=20,
        choices=ATOM_MODAL_LAYOUT_RIGHT,
        default='desc_right',
        help_text='Choose what to show in the '
                  'right side of a atom modal window.')

    related_atoms = models.ManyToManyField(
        "self",
        verbose_name=_("Related Atoms"),
        # through='BlogAtomRelatedAtomMeta',
        related_name='related',
        symmetrical=False,
        blank=True)

    embedded_content = models.TextField(
        blank=True,
        verbose_name=_("HTML and <iframe>"))

    class Meta:
        verbose_name = _("Atom")
        verbose_name_plural = _("Atoms")

    @models.permalink
    def get_absolute_url(self):
        return "article_list_atom", (), {"atom": self.slug}

    def get_absolute_single_url(self):

        """
        Atom absolute url returns a list of related articles, but
        atom can also behave as a single post. For that, use this.
        """

        return '{0}'.format(self.get_absolute_url())

    def get_social_title(self):
        """
        Return `self.social_title` if it exists. Else return `self.title`.
        """
        if hasattr(self, 'social_title') and self.social_title:
            return self.social_title
        else:
            return self.title

    def save(self, *args, **kwargs):
        if not self.headline:
            self.headline = self.title
        super(Atom, self).save(*args, **kwargs)