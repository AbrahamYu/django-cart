from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Mata:
        model = ReviewRating
        fields = ['subject', 'review', 'ratijng']