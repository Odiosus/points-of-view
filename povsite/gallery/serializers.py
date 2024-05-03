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


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'slug',
            'description',
            'image_project',
            'title_block_description',
            'block_description_one',
            'image_block_one',
            'block_description_two',
            'image_block_two',
            'implementation',
            'what_block',
            'time_add',
            'time_update',
            'is_published',
        ]


class ThemesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Themes
        fields = [
            'name',
        ]


class LandingPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LandingPage
        fields = [
            'logo_text',
            'logo_header',
            'about_us',
            'about_us_title',
            'about_us_text',
            'projects',
            'team',
            'logo_footer',
        ]


class WhatBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WhatBlock
        fields = [
            'image',
            'title',
            'text',
        ]
