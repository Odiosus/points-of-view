from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Gallery, Author
from modeltranslation.admin import TranslationAdmin


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        'user', 'title', 'author', 'is_published', 'content_text', 'get_html_photo', 'content', 'publication_date',
        'publication_update')
    list_display_links = ('title',)
    list_filter = ('user', 'author', 'is_published', 'publication_date', 'publication_update')
    search_fields = ['user', 'author', 'title', 'content_text']
    ordering = ['-publication_date']
    fields = ('user', 'title', 'author', 'content_text', 'content_picture', 'get_html_photo', 'is_published')
    readonly_fields = ('publication_date', 'publication_update', 'get_html_photo')
    save_on_top = True
    actions = ['set_published', 'set_draft']
    list_editable = ('is_published',)

    def get_html_photo(self, object):
        if object.content_picture:
            return mark_safe(f"<img src='{object.content_picture.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Gallery.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Gallery.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Author)
class AuthorAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('get_html_photo', 'name', 'surname', 'brand_name', 'email', 'phone', 'biography')
    list_display_links = ('name', 'surname', 'brand_name')
    list_filter = ('surname', 'brand_name')
    search_fields = ['name', 'surname', 'brand_name', 'biography', 'email', 'phone']
    ordering = ['-time_add']
    fields = ('name', 'surname', 'patronymic', 'brand_name', 'email', 'phone', 'photo', 'get_html_photo', 'biography')
    readonly_fields = ('time_add', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'
