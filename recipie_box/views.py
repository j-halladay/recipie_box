from django.shortcuts import render
from recipie_box.models import Recipie, Author, RecipieForm
from recipie_box.forms import AddAuthor


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


def addauthor(request, *args, **kwargs):
    html = 'addauthor.html'

    if request.method == "POST":
        form = AddAuthor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"]
            )

    form = AddAuthor()

    return render(request, html, {'addauthor': form})


def addrecipie(request, *args, **kwargs):
    html = 'addrecipie.html'

    if request.method == "POST":

        form = RecipieForm(request.POST)
        if form.is_valid():

            new_recipie = form.save()

    form = RecipieForm()

    return render(request, html, {'addrecipie': form})
