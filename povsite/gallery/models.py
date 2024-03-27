from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.
class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')  # TODO models.SET_NULL
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content_text = models.TextField(default=None, blank=True, null=True, verbose_name='Статья')
    content_picture = models.ImageField(default=None, blank=True, null=True, verbose_name='Картинка')
    content_audio = FroalaField(default=None, blank=True, null=True, verbose_name='Аудио')
    content_video = FroalaField(default=None, blank=True, null=True, verbose_name='Видео')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    publication_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=False, verbose_name='Статус публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
