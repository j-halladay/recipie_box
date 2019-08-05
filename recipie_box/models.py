from django.db import models
from django.forms import ModelForm


class Author(models.Model):
    name = models.CharField(max_length=40)
    bio = models.CharField(max_length=150)


class Recipie(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    time = models.IntegerField()
    instructions = models.CharField(max_length=500)


class RecipieForm(ModelForm):
    class Meta:
        model = Recipie
        fields = "__all__"
