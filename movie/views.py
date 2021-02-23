from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movie.models import Movie


class MovieView(ListView):
    """Вывод всех фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class MovieDetailView(DetailView):
    """Описание определенного фильма"""
    model = Movie
    slug_field = 'url'
