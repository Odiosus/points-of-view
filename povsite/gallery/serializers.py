from .models import Gallery
from rest_framework import serializers

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = ['user',
                  'title',
                  'content_text',
                  'content_picture',
                  'content_audio',
                  'content_video',
                  'publication_date',
                  'publication_update',
                  'is_published',
                  ]