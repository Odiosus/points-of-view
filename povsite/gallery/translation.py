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
        'surname',
        'brand_name',
        'patronymic',
        'biography',
    )


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'title_block_description',
        'block_description_one',
        'block_description_two',
    )


@register(Themes)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('name',)
