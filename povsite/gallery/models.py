from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.
class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')  # TODO models.SET_NULL
    author = models.ForeignKey('Author', null=True, default=None, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content_text = models.TextField(default=None, blank=True, null=True, verbose_name='Статья')
    content_picture = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True,
                                        verbose_name="Картинка")
    content = models.FileField(default=None, blank=True, null=True, verbose_name='Аудио/Видео')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    publication_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=False, verbose_name='Статус публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class Author(models.Model):
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, blank=True, default=None,  verbose_name='Отчество')
    brand_name = models.CharField(max_length=100, blank=True, verbose_name='Бренд')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения записи')

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.brand_name}, {self.email}, {self.phone}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
