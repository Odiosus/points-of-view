from pprint import pprint

from django.shortcuts import render, redirect
from .models import Gallery, Themes, Feedback
from .serializers import GallerySerializer
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from .forms import FeedbackMultipleChoiceForm


class GalleryList(ListView):
    model = Gallery
    ordering = '-publication_date'
    template_name = 'index.html'
    context_object_name = 'units'
    form = FeedbackMultipleChoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request):
        if request.method == 'POST':
            form = FeedbackMultipleChoiceForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('/')

class GalleryDetail(DetailView):
    model = Gallery
    template_name = 'detail.html'
    context_object_name = 'unit'


#==========================================
#Viewsets

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

