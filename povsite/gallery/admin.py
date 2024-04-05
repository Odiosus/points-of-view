from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Gallery, Author, Feedback, CategoryProject
from modeltranslation.admin import TranslationAdmin


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        'user', 'is_published', 'project', 'short_description_field_title', 'author', 'short_description_field',
        'get_html_photo', 'content', 'publication_date', 'publication_update')
    list_display_links = ('short_description_field_title',)
    list_filter = ('user', 'author', 'is_published', 'project__name', 'publication_date', 'publication_update')
    search_fields = ['title', 'content_text']
    ordering = ['-publication_date']
    readonly_fields = ('publication_date', 'publication_update', 'get_html_photo')
    save_on_top = True
    actions = ['set_published', 'set_draft']
    list_editable = ('is_published',)
    list_per_page = 10
    fieldsets = (
        ("Информация о пользователе", {
            "fields": ("user",),
        }),
        ("Публикация", {
            "fields": ("author", 'project', "title",),
        }),
        ("Написать статью", {
            "classes": ("collapse",),
            "fields": (("content_text",),)
        }),
        ("Добавить медиаконтент", {
            "classes": ["collapse"],
            "description": "Здесь можно добавить аудио/видео или изображение",
            "fields": (("content",),)
        }),
        (None, {
            "fields": ("content_picture", "get_html_photo",)
        }),
        ("Публикуем?", {
            "fields": ("is_published", 'publication_date', 'publication_update',)
        }),
    )

    def get_html_photo(self, object):
        if object.content_picture:
            return mark_safe(f"<img src='{object.content_picture.url}' width=80>")

    get_html_photo.short_description = 'Миниатюра'

    def short_description_field(self, obj):
        if obj.content_text:
            return obj.content_text[:40] + '...' if len(obj.content_text) > 40 else obj.content_text

    short_description_field.short_description = 'Краткое описание'

    def short_description_field_title(self, obj):
        if obj.title:
            return obj.title[:20] + '...' if len(obj.title) > 20 else obj.title

    short_description_field_title.short_description = 'Заголовок'

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
    list_display = ('get_html_photo', 'brand_name', 'name', 'surname', 'email', 'phone', 'short_description_field')
    list_display_links = ('name', 'surname', 'brand_name')
    list_filter = ('surname', 'brand_name')
    search_fields = ['name', 'surname', 'brand_name', 'biography', 'email', 'phone']
    ordering = ['-time_add']
    readonly_fields = ('time_add', 'time_update', 'get_html_photo')
    save_on_top = True
    fieldsets = (
        ("Информация об авторе", {
            "fields": ("brand_name", ("email", "phone"),)
        }),
        ("Персональная информация", {
            "classes": ("collapse",),
            "fields": (("name", "surname", "patronymic",),)
        }),
        ("Биография", {
            "classes": ("collapse",),
            "fields": (("biography",),)
        }),
        (None, {
            "fields": (("photo", "get_html_photo",),)
        }),
        (None, {
            "fields": (('time_add', 'time_update',),)
        }),
    )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'

    def short_description_field(self, obj):
        if obj.biography:
            return obj.biography[:40] + '...' if len(obj.biography) > 40 else obj.biography

    short_description_field.short_description = 'Биография'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('theme', 'name', 'email', 'short_description_field', 'time_add')
    list_display_links = ('name', 'email')
    list_filter = ('theme', 'name', 'email', 'time_add')
    search_fields = ['name', 'email', 'message']
    ordering = ['-time_add']
    save_on_top = True
    fields = ('theme', 'name', 'email', 'message', 'time_add')
    readonly_fields = ('theme', 'name', 'email', 'message', 'time_add',)
    list_per_page = 10

    def short_description_field(self, obj):
        if obj.message:
            return obj.message[:40] + '...' if len(obj.message) > 40 else obj.message

    short_description_field.short_description = 'Сообщение'


@admin.register(CategoryProject)
class CategoryProjectAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('name', 'short_description_field')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ['name', 'description']
    save_on_top = True
    fieldsets = (
        ("Проект", {
            "fields": ("name",)
        }),
        ("Описание проекта", {
            "classes": ("collapse",),
            "fields": (("description",),)
        }),
    )

    def short_description_field(self, obj):
        if obj.description:
            return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description

    short_description_field.short_description = 'Краткое описание'


admin.site.site_header = 'Арт-лаборатория "Точки Зрения", открывающая искусство по-новому'
admin.site.site_title = 'Лаборатория "Точки Зрения"'
# admin.site.index_title = 'Администрирование лаборатории "Точки Зрения"'
