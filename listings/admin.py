from django.contrib import admin

# Register your models here.
from .models import Listing

# Administration Screen - Selecting columns to be listed for listing table


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'zipcode',
                    'realtor', 'is_published')
    list_display_links = ('id', 'title', )
    list_filter = ('zipcode', 'city', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('zipcode', 'city',)
    list_per_page = 3


admin.site.register(Listing, ListingAdmin)
