from django.contrib import admin
from .models import Gallery
from modeltranslation.admin import TranslationAdmin


class GalleryAdmin(TranslationAdmin):
    model = Gallery


admin.site.register(Gallery)