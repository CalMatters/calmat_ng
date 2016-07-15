from __future__ import unicode_literals

import stripe
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete
from media_manager.models import MediaItem
from sites.models import TimeStamped

from .signals import delete_stripe_customer

#-------------------------------------------------------------------------------
#   :: Donation Page
#-------------------------------------------------------------------------------

class Donate(TimeStamped):

    name = models.CharField(
        max_length=50,
        help_text="Used for internal tracking only.")

    donate_message_image = models.ForeignKey(
        MediaItem,
        verbose_name="Donation top box image",
        null=True,
        blank=True,
        related_name="donation_top_box_image")

    donate_message = models.TextField(
        verbose_name='Donation top box message',
        blank=True,
        default="",
        help_text='Top orange box Donate text. Use CSS class .message-text \
                   for the messange, and .message-attribution for the \
                   quote attribution.')

    donate_section_top = models.TextField(
        verbose_name='Donate section top',
        blank=True,
        default="",
        help_text='Content box for the Donate section above the blue links.')

    donate_section_bottom = models.TextField(
        verbose_name='Donate section bottom',
        blank=True,
        default="",
        help_text='Content box for the Donate section below the blue links.')

    donation_values = models.CharField(
        verbose_name='Donation values',
        max_length=80,
        blank=True,
        default="25,100,250,Other",
        help_text='Enter donation values separated by commas. DO NOT INCLUDE "$". \
                   Commas will be added to values over $1,000 automatically.')
    
    tell_section = models.TextField(
        verbose_name='Tell your friends',
        blank=True,
        default="",
        help_text='Text for the Tell your friends section of \
                    the Donate page.')
        
    class Meta:
        verbose_name = _("Donate Page")
        verbose_name_plural = _("Donate Page")
        get_latest_by = 'created'
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = 'Main Donate Page Settings'
        super(Donate, self).save(*args, **kwargs)

    def donation_values_list(self):
        """
        Return a list of donation values to be output in the blue buttons on
        the Donation page. Values >= 1,000 will have commas added by humanize
        Django tempage tag.
        """
        values = self.donation_values.split(',')

        values_list = []
        for v in values:
            try:
                val = int(v)
                text = '${0}'.format(val)
                values_list.append({'val': val, 'text': text})
            except ValueError:
                values_list.append({'val': v.lower(), 'text': v.capitalize()})

        print(values_list)
        return values_list

#-------------------------------------------------------------------------------
#   :: Stripe Related
#-------------------------------------------------------------------------------

class StripeCustomer(models.Model):
    """
    
    """
    AMOUNT_CHOICES = [
        ('100','$100'),
        ('250','$250'),
        ('1000','$1000'),
        ('0','Other'),
    ]
    stripe_id = models.CharField('Stripe ID',max_length=140,blank=True,null=True)
    stripe_email = models.EmailField('email')
    
    first_name = models.CharField('first name',max_length=140)
    last_name = models.CharField('last name',max_length=140)
    phone = models.CharField('phone',max_length=140)
    address1 = models.CharField('address 1',max_length=140)
    address2 = models.CharField('address 2',max_length=140,blank=True,null=True)
    city = models.CharField('city',max_length=140)
    state = models.CharField('state',max_length=140)
    zip_code = models.CharField('zip code',max_length=10)
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("stripe customer")
        verbose_name_plural = _("stripe customers")
        get_latest_by = 'created'
    
    def __str__(self):
        return self.stripe_email
        
    def save(self, *args, **kwargs):
        super(StripeCustomer, self).save(*args, **kwargs)
    
    def full_name(self):
    	return u'%s %s' % (self.first_name,self.last_name)
    	
post_delete.connect(delete_stripe_customer, sender=StripeCustomer)