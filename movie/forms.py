from django import forms

from movie.models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
