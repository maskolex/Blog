from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create', 'is_published')

admin.site.register(Women, WomenAdmin)
admin.site.register(Category)
