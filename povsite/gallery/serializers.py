from .models import *
from rest_framework import serializers


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [
            'user',
            'author',
            'title',
            'content_text',
            'content_picture',
            'content',
            'publication_date',
            'publication_update',
            'is_published',
            'project',
            'objects',
            'published',
        ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            'email',
            'phone',
            'name',
            'surname',
            'patronymic',
            'photo',
            'brand_name',
            'biography',
            'time_add',
            'time_update',
        ]


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'theme',
            'name',
            'email',
            'message',
            'time_add',
        ]


class CategoryProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryProject
        fields = [
            'name',
            'description',
        ]


class ThemesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Themes
        fields = [
            'name',
        ]
