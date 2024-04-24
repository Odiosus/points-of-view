from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework.generics import get_object_or_404

from .models import Gallery, Themes, Feedback, Project
from .serializers import GallerySerializer
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from .forms import FeedbackMultipleChoiceForm


class ProjectList(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'
    form = FeedbackMultipleChoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['authors'] = Author.objects.all()
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
        context['galleries'] = Gallery.objects.filter(project=context['object'])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Project, slug=self.kwargs[self.slug_url_kwarg])

# class ProjectDetail(DetailView):
#     model = Project
#     slug_url_kwarg = 'project_slug'
#     template_name = 'detail.html'
#     context_object_name = 'unit'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Project, slug=self.kwargs[self.slug_url_kwarg])


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