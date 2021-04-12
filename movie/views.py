from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movie.models import Movie
from movie.forms import ReviewForm


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


class AddReview(View):
    """Отправка отзывов"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
