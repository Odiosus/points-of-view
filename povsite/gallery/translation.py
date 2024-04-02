from .models import Gallery, Author
from modeltranslation.translator import register, TranslationOptions


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'content_text', 'content')


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'brand_name', 'biography')
