from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Category, Prestataire, Ville
# Register your models here.

class PrestataireAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'city', 'category')
    list_filter = ('title', 'slug', 'city', 'category')
    search_fields = ('title', 'Category','city')
    prepopulated_fields = {'slug': ('title',),'longitude':('position.y',),'latitude':('position.x',)}

admin.site.register(Prestataire, PrestataireAdmin)

class CategoryAdmin(SummernoteModelAdmin):
    list_display=('name','slug')
    list_filter=('name','slug')
    search_fields=('name','slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class VilleAdmin(SummernoteModelAdmin):
    list_display=('ville','slug')
    list_filter=('ville','slug')
    search_fields=('ville','slug')
    prepopulated_fields = {'slug': ('ville',)}
admin.site.register(Ville,VilleAdmin)
