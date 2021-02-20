from django.urls import path

from movie import views as movie

urlpatterns = [
    path('', movie.MovieView.as_view()),
]
