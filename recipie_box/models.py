from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40)
    bio = models.CharField(max_length=150)


class Recipie(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    time = models.IntegerField()
    instructions = models.CharField(max_length=500)
