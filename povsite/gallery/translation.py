from .models import Gallery, Author
from modeltranslation.translator import register, TranslationOptions


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'content_picture',)


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'brand_name',)  # TODO 'patronymic', 'email', 'phone'?
