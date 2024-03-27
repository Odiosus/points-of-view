from django.contrib import admin
from .models import Gallery


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ['name']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content_text', 'content_picture', 'publication_date')
    list_display_links = ('title', 'content_text')
    list_filter = ('content_text', 'publication_date',)
    search_fields = ['user', 'title', 'content_text']
    ordering = ['-publication_date']
