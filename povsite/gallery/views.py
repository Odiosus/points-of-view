from django.shortcuts import render
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework import viewsets
from django.views.generic import ListView, DetailView


#Функциональное вью или дженерик?


class GalleryList(ListView):
    model = Gallery
    ordering = '-publication_date'
    template_name = 'index.html'
    context_object_name = 'units'

class GalleryDetail(DetailView):
    model = Gallery
    template_name = 'detail.html'
    context_object_name = 'unit'

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

