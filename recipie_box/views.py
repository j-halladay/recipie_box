from django.shortcuts import render
from recipie_box.models import Recipie, Author


def index(request, *args, **kwargs):
    html = 'index.html'
    items = Recipie.objects.all()
    return render(request, html, {"recipies": items})


def recipie(request, id, *args, **kwargs):
    html = 'recipie.html'
    item = Recipie.objects.get(id=id)
    return render(request, html, {'recipie': item})


def author(request, id, *args, **kwargs):
    html = 'author.html'
    item = Author.objects.get(id=id)
    items = Recipie.objects.all().filter(author=item)
    return render(request, html, {'author': item, "recipies": items})
