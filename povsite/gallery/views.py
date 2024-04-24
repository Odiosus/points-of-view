from pprint import pprint

from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

from .models import Gallery, Themes, Feedback, Project
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
                # feed = Feedback(
                #     name=form.cleaned_data['name'],
                #     theme=Themes.objects.get(pk=form.cleaned_data['theme']),
                #     email=form.cleaned_data['email'],
                #     message=form.cleaned_data['message'],
                # )
                form.save()
                pprint(request.POST)
                pprint(Themes.objects.values('pk'))
                pprint(Themes.objects.values_list('pk', flat=True))

            else:
                pprint(request.POST)
                pprint(Themes.objects.values('pk'))
                pprint(Themes.objects.values_list('pk', flat=True))
        return redirect('/')


class GalleryDetail(DetailView):
    model = Gallery
    template_name = 'detail.html'
    context_object_name = 'unit'

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Project, slug=self.kwargs[self.slug_url_kwarg])

class ProjectDetail(DetailView):
    model = Project
    slug_url_kwarg = 'project_slug'
    template_name = 'detail.html'
    context_object_name = 'unit'

    def get_object(self, queryset=None):
        return get_object_or_404(Project, slug=self.kwargs[self.slug_url_kwarg])


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
