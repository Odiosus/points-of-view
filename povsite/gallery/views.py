from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework.generics import get_object_or_404

from .models import Gallery, Themes, Feedback, Project
from .serializers import GallerySerializer
from rest_framework import viewsets
from django.views.generic import TemplateView, DetailView
from .forms import FeedbackMultipleChoiceForm


class StartPageView(TemplateView):
    template_name = 'index.html'
    form = FeedbackMultipleChoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['authors'] = Author.objects.all()
        context['projects'] = Project.objects.all()
        context['start_page'] = StartPage.objects.first()
        return context

    def post(self, request):
        if request.method == 'POST':
            form = FeedbackMultipleChoiceForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('/')


class ProjectDetail(DetailView):
    model = Project
    slug_url_kwarg = 'project_slug'
    template_name = 'detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.filter(implementation=context['object'])
        context['what_block'] = WhatBlock.objects.filter(what_block=context['object'])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Project.published, slug=self.kwargs[self.slug_url_kwarg])


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
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ThemesViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all()
    serializer_class = ThemesSerializer
