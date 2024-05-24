# Generated by Django 5.0.3 on 2024-04-25 07:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_whatblock_remove_project_implementation_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='author',
            name='patronymic_en',
        ),
        migrations.RemoveField(
            model_name='author',
            name='patronymic_fr',
        ),
        migrations.RemoveField(
            model_name='author',
            name='patronymic_ru',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='is_published',
        ),
        migrations.AddField(
            model_name='project',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус публикации'),
        ),
        migrations.AddField(
            model_name='project',
            name='what_block',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.whatblock', verbose_name='Что мы умеем?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='implementation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery', verbose_name='Проекты'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(help_text='это поле заполняется автоматически', max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='URL'),
        ),
    ]