from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Gallery, Author, Feedback, Project, Themes, LandingPage, WhatBlock
from modeltranslation.admin import TranslationAdmin


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        'user', 'get_html_photo', 'title', 'author', 'short_description_field',
        'content', 'publication_date', 'publication_update')
    list_display_links = ('title',)
    list_filter = ('user', 'author', 'publication_date', 'publication_update')
    search_fields = ['title', 'content_text']
    ordering = ['-publication_date']
    readonly_fields = ('publication_date', 'publication_update', 'get_html_photo')
    save_on_top = True
    list_per_page = 10
    fieldsets = (
        ("Информация о пользователе", {
            "fields": ("user",),
        }),
        ("Публикация", {
            "fields": ("author", "title",),
        }),
        ("Написать статью", {
            "classes": ("collapse",),
            "fields": (("content_text",),)
        }),
        ("Добавить медиаконтент", {
            "classes": ["collapse"],
            "description": "Здесь можно добавить аудио/видео контент",
            "fields": (("content",),)
        }),
        (None, {
            "fields": ("content_picture", "get_html_photo",)
        }),
        ("Публикуем?", {
            "fields": ('publication_date', 'publication_update',)
        }),
    )

    def get_html_photo(self, object):
        if object.content_picture:
            return mark_safe(f"<img src='{object.content_picture.url}' height=50 width=70>")

    get_html_photo.short_description = 'Миниатюра'

    def short_description_field(self, obj):
        if obj.content_text:
            return obj.content_text[:40] + '...' if len(obj.content_text) > 40 else obj.content_text

    short_description_field.short_description = 'Краткое описание'


@admin.register(Author)
class AuthorAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('get_html_photo', 'brand_name', 'name', 'email', 'phone', 'short_description_field')
    list_display_links = ('name', 'brand_name')
    list_filter = ('brand_name',)
    search_fields = ['name', 'brand_name', 'biography', 'email', 'phone', 'short_description_field']
    ordering = ['-time_add']
    readonly_fields = ('time_add', 'time_update', 'get_html_photo')
    save_on_top = True
    save_as = True
    list_per_page = 10
    fieldsets = (
        ("Информация об авторе", {
            "fields": ("name", "brand_name", "email", "phone",)
        }),
        ("Биография", {
            "classes": ("collapse",),
            "fields": (("biography",),)
        }),
        (None, {
            "fields": ("photo", "get_html_photo",),
        }),
        (None, {
            "fields": ('time_add', 'time_update',)
        }),
    )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'

    def short_description_field(self, obj):
        if obj.biography:
            return obj.biography[:100] + '...' if len(obj.biography) > 100 else obj.biography

    short_description_field.short_description = 'Биография'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('theme', 'name', 'email', 'short_description_field', 'time_add')
    list_display_links = ('name', 'email')
    list_filter = ('theme__name', 'name', 'time_add')
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


@admin.register(Project)
class ProjectAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('name', 'is_published', 'get_html_image_project', 'short_title_block_description_field')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)
    list_filter = ('name', 'is_published', 'time_add', 'time_update')
    search_fields = ['name']
    save_on_top = True
    save_as = True
    ordering = ['-time_add']
    actions = ['set_published', 'set_draft']
    list_editable = ('is_published',)
    readonly_fields = ('time_add', 'time_update', 'short_title_block_description_field', 'get_html_image_project')
    list_per_page = 10
    fieldsets = (
        ("Проект", {
            "fields": ("name", 'slug', 'description', 'image_project',)
        }),
        ("Описание проекта — Блок 1", {
            "classes": ("collapse",),
            "fields": ('title_block_description', 'block_description_one', 'image_block_one',),
        }),
        ("Описание проекта — Блок 2", {
            "classes": ("collapse",),
            "fields": ('block_description_two', 'image_block_two',),
        }),
        ("Реализация: выбираем галереи", {
            "classes": ("collapse",),
            "description": "Здесь нужно выбрать все галереи по этому проекту",
            "fields": ("implementation",)
        }),
        ("Что мы умеем", {
            "classes": ("collapse",),
            "description": "Здесь нужно выбрать наши отличительные особенности по этому проекту",
            "fields": ("what_block",)
        }),
        ("Публикуем?", {
            "fields": ("is_published", 'time_add', 'time_update',)
        }),
    )

    def short_title_block_description_field(self, obj):
        if obj.title_block_description:
            return obj.title_block_description[:100] + '...' if len(
                obj.title_block_description) > 100 else obj.title_block_description

    short_title_block_description_field.short_description = 'Краткое описание'

    def get_html_image_project(self, object):
        if object.image_project:
            return mark_safe(f"<img src='{object.image_project.url}' width=50>")

    get_html_image_project.short_description = 'Изображение'

    @admin.action(description="Опубликовать выбранные проекты")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Project.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записей.")

    @admin.action(description="Снять с публикации выбранные проекты")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Project.Status.DRAFT)
        self.message_user(request, f"{count} проекта сняты с публикации!", messages.WARNING)


@admin.register(Themes)
class ThemesAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ['name']
    save_on_top = True
    fields = ('name',)


@admin.register(LandingPage)
class LandingPageAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('logo_text', 'get_html_logo_header',)
    list_display_links = ('logo_text',)
    list_filter = ('logo_text',)
    search_fields = ['logo_text']
    save_on_top = True
    readonly_fields = ('get_html_logo_header', 'get_html_logo_footer')
    fieldsets = (
        ("Хедер", {
            "classes": ("collapse",),
            "fields": ("logo_text", 'logo_header',)
        }),
        ("О нас", {
            "classes": ("collapse",),
            "fields": ('about_us', 'about_us_title', 'about_us_text',),
        }),
        ("Проекты", {
            "fields": ("projects",)
        }),
        ("Команда", {
            "fields": ("team",)
        }),
        ("Футер", {
            "classes": ("collapse",),
            "fields": ('logo_footer',),
        }),
    )

    def get_html_logo_header(self, object):
        if object.logo_header:
            return mark_safe(f"<img src='{object.logo_header.url}' width=50>")

    get_html_logo_header.short_description = 'Лого Хедера'

    def get_html_logo_footer(self, object):
        if object.logo_footer:
            return mark_safe(f"<img src='{object.logo_footer.url}' width=50>")

    get_html_logo_footer.short_description = 'Лого Футера'


@admin.register(WhatBlock)
class WhatBlockAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('get_html_image', 'title', 'text', 'short_text_field')
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ['title', ]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_html_image',)
    list_per_page = 10
    fieldsets = (
        ("Имя блока: Что мы умеем?", {
            "fields": ("title",)
        }),
        ("Описание скилла", {
            "classes": ("collapse",),
            "fields": ('text', )
        }),
        ("Изображение скилла", {
            "fields": ("image", 'get_html_image')
        }),
    )

    def short_text_field(self, obj):
        if obj.text:
            return obj.text[:100] + '...' if len(obj.text) > 100 else obj.text

    short_text_field.short_description = 'Краткое описание'

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_image.short_description = 'Символ скилла'


admin.site.site_header = 'Арт-лаборатория "Точки Зрения", открывающая искусство по-новому'
admin.site.site_title = 'Лаборатория "Точки Зрения"'
# admin.site.index_title = 'Администрирование лаборатории "Точки Зрения"'
