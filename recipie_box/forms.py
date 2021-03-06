from django import forms
from recipie_box.models import Author


class AddAuthor(forms.Form):
    username = forms.CharField(max_length=30)
    name = forms.CharField(max_length=40)
    bio = forms.CharField(max_length=150)
    is_staff = forms.BooleanField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
