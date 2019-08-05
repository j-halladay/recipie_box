from django import forms
from recipie_box.models import Author


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=40)
    bio = forms.CharField(max_length=150)
