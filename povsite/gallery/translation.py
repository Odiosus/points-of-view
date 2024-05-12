from .models import *
from modeltranslation.translator import register, TranslationOptions


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'content_text',
        'content',
    )


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = (
        'name',
        # 'photo',
        # 'brand_name',
        'biography',
    )


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'svg_logo',
        'description',
        'title_block_description_one',
        'block_description_one',
        'title_block_description_two',
        'block_description_two',
    )


@register(Themes)
class GalleryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(StartPage)
class StartPageTranslationOptions(TranslationOptions):
    fields = (
        'logo_text',
        'logo_main',
        'logo_header',
        'about_us',
        'about_us_title',
        'about_us_text',
        'logo_footer',)


@register(WhatBlock)
class WhatBlockTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'text',)
