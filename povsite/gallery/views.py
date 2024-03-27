from django.shortcuts import render
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework import viewsets
from django.views.generic import ListView


#Функциональное вью или дженерик?


class GalleryList(ListView):
    model = Gallery
    ordering = '-publication_date'
    template_name = 'index.html'
    context_object_name = 'units'

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer