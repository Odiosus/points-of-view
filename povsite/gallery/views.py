from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from .forms import FeedbackMultipleChoiceForm


class CategoryProjectList(ListView):
    model = CategoryProject
    template_name = 'index.html'
    context_object_name = 'projects'
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

class CategoryProjectDetail(DetailView):
    model = CategoryProject
    template_name = 'detail.html'
    context_object_name = 'unit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.filter(project=context['object'])
        return context



#==========================================
#Viewsets

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CategoryProjectViewSet(viewsets.ModelViewSet):
    queryset = CategoryProject.objects.all()
    serializer_class = CategoryProjectSerializer


class ThemesViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all()
    serializer_class = ThemesSerializer