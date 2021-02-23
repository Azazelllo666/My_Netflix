from django.urls import path

from movie import views as movie

urlpatterns = [
    path('', movie.MovieView.as_view(), name='movie_list'),
    path('<slug:slug>/', movie.MovieDetailView.as_view(), name='movie_detail'),
]
