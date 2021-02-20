from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import View

from movie.models import Movie


class MovieView(ListView):
    """Описание фильма"""
    model = Movie
    template_name = 'movie/movies.html'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
