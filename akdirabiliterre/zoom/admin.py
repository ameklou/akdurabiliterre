from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Zoom
# Register your models here.

class ZoomAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','architect', 'author', 'publish','status')
    list_filter = ('status', 'created','architect', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(Zoom, ZoomAdmin)
