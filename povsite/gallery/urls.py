from django.urls import path
from .views import GalleryList


urlpatterns = [
    path('', GalleryList.as_view(), name='main')
]
