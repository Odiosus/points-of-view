from django.contrib import admin
from .models import Gallery
from modeltranslation.admin import TranslationAdmin


class GalleryAdmin(TranslationAdmin):
    model = Gallery



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ['name']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'is_published', 'content_text', 'content_picture', 'publication_date', 'publication_update')
    list_display_links = ('title', )
    list_filter = ('title', 'publication_date', 'publication_update')
    search_fields = ['user', 'title', 'content_text']
    ordering = ['-publication_date']
