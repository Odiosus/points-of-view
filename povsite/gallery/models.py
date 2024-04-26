from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Project.Status.PUBLISHED)


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    author = models.ForeignKey('Author', null=True, default=None, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=80, verbose_name='Заголовок')
    content_text = models.TextField(default=None, blank=True, null=True, verbose_name='Статья')
    content_picture = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True,
                                        verbose_name="Изображение")
    content = models.FileField(upload_to="files/%Y/%m/%d/", default=None, blank=True, null=True,
                               verbose_name='Аудио/Видео')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    publication_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Author(models.Model):
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    name = models.CharField(max_length=100, verbose_name='Имя и фамилия')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    brand_name = models.CharField(max_length=100, verbose_name='Бренд')
    biography = models.TextField(default=None, blank=True, null=True, verbose_name='Биография')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения записи')

    def __str__(self):
        return f'{self.name}: "{self.brand_name}"'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Feedback(models.Model):
    theme = models.ForeignKey('Themes', on_delete=models.CASCADE, default='no subject', verbose_name='Тема')
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления записи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Project(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    name = models.CharField(max_length=50, verbose_name='Название проекта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", validators=[
        MinLengthValidator(5, message="Минимум 5 символов"),
        MaxLengthValidator(100, message="Максимум 100 символов"),
    ], help_text="это поле заполняется автоматически")
    description = models.CharField(max_length=50, verbose_name='Слоган')
    image_project = models.ImageField(upload_to="photos_project/%Y/%m/%d/", default=None, blank=True, null=True,
                                      verbose_name="Титульное изображение")
    title_block_description = models.CharField(max_length=150, verbose_name='Заголовок блока описания')
    block_description_one = models.TextField(max_length=500, verbose_name='Описание блока No1')
    image_block_one = models.ImageField(upload_to="photos_project/block1/%Y/%m/%d/", default=None, blank=True,
                                        null=True, verbose_name="Изображение блока No1")
    block_description_two = models.TextField(max_length=500, verbose_name='Описание блока No2')
    image_block_two = models.ImageField(upload_to="photos_project/block2/%Y/%m/%d/", default=None, blank=True,
                                        null=True, verbose_name="Изображение блока No2")
    implementation = models.ManyToManyField(Gallery, verbose_name='Галереи', related_name='implementation')
    what_block = models.ManyToManyField('WhatBlock', verbose_name='Наши скиллы', related_name='what_block')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения записи')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT,
                                       verbose_name='Статус публикации')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('projects', kwargs={'project_slug': self.slug})


class Themes(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тема обращения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема обращения обратной связи'
        verbose_name_plural = 'Темы обращений обратной связи'


class LandingPage(models.Model):
    logo_text = models.CharField(max_length=50, verbose_name="Название логотипа")
    logo_header = models.ImageField(upload_to="logo_landing/", default=None, blank=True, null=True,
                                    verbose_name="Логотип хедера")
    about_us = models.CharField(max_length=50, verbose_name="О нас")
    about_us_title = models.CharField(max_length=100, verbose_name="Заголовок раздела")
    about_us_text = models.TextField(max_length=500, verbose_name="Текст раздела")
    projects = models.ManyToManyField(Project, verbose_name="Проекты", related_name="projects")
    team = models.ManyToManyField(Author, verbose_name="Команда", related_name="team")
    logo_footer = models.ImageField(upload_to="logo_footer/", default=None, blank=True, null=True,
                                    verbose_name="Логотип футера")

    def __str__(self):
        return self.logo_text

    class Meta:
        verbose_name = 'Основная страница'
        verbose_name_plural = 'Основная страница'


class WhatBlock(models.Model):
    image = models.ImageField(upload_to="photos_what_block/", default=None, blank=True, null=True,
                              verbose_name="Изображение скилла")
    title = models.CharField(max_length=50, verbose_name="Название скилла")
    text = models.CharField(max_length=255, verbose_name="Описание скилла")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Что мы умеем?'
        verbose_name_plural = 'Что мы умеем?'
