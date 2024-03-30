from .models import Gallery, Author
from modeltranslation.translator import register, TranslationOptions


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'content_picture', 'content', 'content_text', )


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'patronymic', 'brand_name',)
