from django.contrib import admin
from .models import Realtor

# Administration Screen - Columns to be listed


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_mvp')
    list_display_links = ('name', 'phone', 'email')
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    search_fields = ('name', 'phone', 'email')


admin.site.register(Realtor, RealtorAdmin)
