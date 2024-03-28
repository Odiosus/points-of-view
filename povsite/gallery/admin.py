from django.contrib import admin
from django.utils.safestring import mark_safe

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
        'user', 'title', 'is_published', 'content_text', 'get_html_photo', 'publication_date', 'publication_update')
    list_display_links = ('title',)
    list_filter = ('title', 'publication_date', 'publication_update')
    search_fields = ['user', 'title', 'content_text']
    ordering = ['-publication_date']
    fields = ('user', 'title', 'content_text', 'content_picture', 'get_html_photo', 'is_published')
    readonly_fields = ('publication_date', 'publication_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.content_picture:
            return mark_safe(f"<img src='{object.content_picture.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'
