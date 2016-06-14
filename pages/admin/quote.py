from django.contrib import admin

from pages.models import Quote


class QuoteAdmin(admin.ModelAdmin):

    # Todo:  Move to Admin super class parallel with ContentContainer is Sites
    class Media:
        js = (
            'https://cdn.tinymce.com/4/tinymce.min.js',
            'theme/js/tinymce_ng.js'
        )
        css = {
            'all': (
            )
        }

    list_display = ('title', )
    fieldsets = (
        ('Content', {"fields": (
            "title",
            "content",
            "attribution",
            "custom_link",
        )}),
    )
admin.site.register(Quote, QuoteAdmin)