from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Category, Prestataire, Ville
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PrestataireAdmin(LeafletGeoAdmin,SummernoteModelAdmin):
    settings_overrides = {
       'DEFAULT_CENTER': (6.13, 1.22),
       'DEFAULT_ZOOM':17
    }
    list_display = ('title', 'slug', 'city', 'category')
    list_filter = ('title', 'slug', 'city', 'category')
    search_fields = ('title', 'Category','city')
    prepopulated_fields = {'slug': ('title',)}

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
