from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.
class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content_text = models.TextField()
    content_picture = models.ImageField()
    content_audio = FroalaField()
    content_video = FroalaField()
    publication_date = models.DateTimeField(auto_now_add=True)
    publication_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
